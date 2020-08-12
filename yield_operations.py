# 收益率有关内容的计算
# 主要涉及：多头收益率，空头收益率，多空组合收益率，分档收益率的计算
import pandas as pd
import numpy as np
import os


def calculate_yield(factor, yield_matrix, low_limit, high_limit, stocks=0, holding_periods=1, method='long', weight_output=0):
    """
    计算分位数位于特定区间的持仓收益（多头与空头）

    Parameters
    ----------
    factor：因子矩阵（pd.DataFrame）
    yield_series：收益率矩阵
    low_limit：计算分位数的百分比下限
    high_limit：计算分位数的百分比上限
    stocks：默认为0，表示不输出选股名称，为1则表示输出选股名称
    holding_periods：调仓周期，默认为每日调仓
    method：做多(long)/做空(short)
    weight_output：默认为0，表示不返回权重矩阵，否则表示返回权重矩阵,这里

    Returns
    -------
    -1：目标方法错误

    根据不同的参数形式有不同的返回值

    Notes
    -------
    注意在实际操作的过程中，T期的因子值只有在T期结束之后才可以获取，所以应当对应的是T+1期到T+2期的收益率
    """
    factor_quantile = factor.quantile([low_limit, high_limit], axis=1).T
    temp = factor.sub(factor_quantile.iloc[:, 0], axis=0) > 0
    temp_temp = (-factor).add(factor_quantile.iloc[:, 1], axis=0) > 0
    temp[-temp_temp] = False
    weight = pd.DataFrame(np.ones((factor.shape[0], factor.shape[1])), index=factor.index, columns=factor.columns)
    weight[-temp] = 0
    date_useful = (np.arange(factor.shape[0]) % holding_periods) == 0
    useful_index = list(weight.index[date_useful])
    for i in range(weight.shape[0]):
        if weight.index[i] not in useful_index:
            weight.iloc[i, :] = (1 + yield_matrix.iloc[i, :]) * weight.iloc[i - 1, :]
    weight = weight.div(np.nansum(weight, axis=1), axis=0)
    weight_copy = weight.copy()
    weight = np.array(weight)
    if stocks == 1:  # 输出股票索引
        stocks_collection = {}
        for i in range(weight.shape[0]):
            temp = weight[i, :]
            temp[np.isnan(temp)] = 0
            stocks_collection[yield_matrix.index[i]] = list(yield_matrix.columns[temp != 0])
    rev = np.array(yield_matrix)
    weight[2:weight.shape[0], :] = weight[0:weight.shape[0] - 2, :]  # 注意Notes中的问题
    weight[0] = 0
    weight[1] = 0
    if method == 'long':  # 做多
        rev_series = np.nansum(weight * rev, axis=1)
        rev_series_cumu = (rev_series + 1).cumprod()
    elif method == 'short': # 做空
        rev_series = np.nansum(-weight * rev, axis=1)
        rev_series_cumu = (1 + rev_series).cumprod()
    else:
        print('目标方法不被识别！')
        return -1

    if stocks == 0 and weight_output == 0:
        return {'yield': {'not_cumu': rev_series, 'cumu': rev_series_cumu}}
    elif stocks == 1 and weight_output == 0:
        return {'yield': {'not_cumu': rev_series, 'cumu': rev_series_cumu},
                'stocks': stocks_collection}
    else:
        if stocks == 1:
            return {'yield': {'not_cumu': rev_series, 'cumu': rev_series_cumu},
                    'stocks': stocks_collection,
                    'weight': weight_copy}
        else:
            return {'yield': {'not_cumu': rev_series, 'cumu': rev_series_cumu},
                    'weight': weight_copy}


def index_yield(index):
    """
    计算指数的收益率序列

    Parameters
    ----------
    index：目标指数序列(pd.DataFrame)

    Returns
    -------
    指数的累计收益率和每阶段收益率


    """
    rev_series = np.array(index.pct_change(periods=1))
    rev_series[0] = 0
    rev_series_cumu = (rev_series + 1).cumprod()
    return {'cumu': rev_series_cumu, 'not_cumu': rev_series}


def Yield(ic, factor_name, holding_periods, percent, factor, yield_matrix):
    """
    计算多头累计超额收益序列，空头累计超额收益序列，多空组合累计超额收益序列（根据持仓周期调整后）

    Parameters
    ----------
    ic：传入因子IC序列
    factor_name：因子名称
    holding_periods：调仓周期
    percent：多（空）百分比
    factor：因子矩阵
    yield_matrix：收益率矩阵

    Returns
    -------

    多头收益序列，空头收益序列，多空组合收益序列，均包括累计与非累计
    具体每个调仓日后的仓中股票会输出在胡赐额结果的文件夹中
    """
    if np.sum(ic>0) >= np.sum(ic<0):
        flag = 1  # 正向因子
    else:
        flag = -1  # 负向因子

    print('准备输出持仓记录...')
    # 可能出现多次回测调试的情况，如果文件已经存在，则将文件都删除
    if os.path.exists('backtest_result/'+factor_name+'/'+factor_name +'_'+str(holding_periods)+'D_stocks_select.txt'):
        print('经检测，此次回测非第一次回测，正在将旧的持仓记录删除...')
        os.remove('backtest_result/'+factor_name+'/'+factor_name +'_'+str(holding_periods)+'D_stocks_select.txt')
        print('删除完毕！')

    '''多头'''
    if flag == 1:
        dic = calculate_yield(
            factor=factor,
            yield_matrix=yield_matrix,
            low_limit=1-percent,
            high_limit=1,
            stocks=1,
            holding_periods=holding_periods,
            method='long',
            weight_output=1)
        long_rev_series_cumu = dic['yield']['cumu']
        long_rev_series = dic['yield']['not_cumu']
        stocks_select = dic['stocks']
        weight = dic['weight']
    else:
        dic = calculate_yield(
            factor=factor,
            yield_matrix=yield_matrix,
            low_limit=0,
            high_limit=percent,
            stocks=1,
            holding_periods=holding_periods,
            method='long',
            weight_output=1)
        long_rev_series_cumu = dic['yield']['cumu']
        long_rev_series = dic['yield']['not_cumu']
        stocks_select = dic['stocks']
        weight = dic['weight']
    file = open('backtest_result/' + factor_name + '/' + factor_name + '_' + str(holding_periods) + 'D_stocks_select.txt', 'w')
    for i in stocks_select.keys():
        file.write(str(i) + '\n')
        file.write(str(stocks_select[i]))
        file.write('\n')
    file.close()

    '''空头'''
    if flag == 1:
        temp = calculate_yield(
            factor=factor,
            yield_matrix=yield_matrix,
            low_limit=0,
            high_limit=percent,
            stocks=0,
            holding_periods=holding_periods,
            method='short')
        short_rev_series_cumu = temp['yield']['cumu']
        short_rev_series = temp['yield']['not_cumu']
    else:
        temp = calculate_yield(
            factor=factor,
            yield_matrix=yield_matrix,
            low_limit=1-percent,
            high_limit=1,
            stocks=0,
            holding_periods=holding_periods,
            method='short')
        short_rev_series_cumu = temp['yield']['cumu']
        short_rev_series = temp['yield']['not_cumu']

    '''多空组合'''
    mix_rev_series_cumu = (long_rev_series_cumu + short_rev_series_cumu) / 2
    mix_rev_series = (long_rev_series + short_rev_series) / 2
    return {
        'long': {'cumu': long_rev_series_cumu, 'not_cumu': long_rev_series},
        'short': {'cumu': short_rev_series_cumu, 'not_cumu': short_rev_series},
        'mix': {'cumu': mix_rev_series_cumu, 'not_cumu': mix_rev_series},
        'weight': weight
        }

def group_yield(holding_periods, factor, yield_matrix, group_number=10):
    """
    计算分档净值曲线（每一档都做多）

    Parameters
    ----------
    holding_periods：调仓周期
    factor：因子矩阵
    close：收盘价矩阵
    group_number：分组数量，默认为10

    Returns
    -------

    """
    width = []
    for i in range(group_number):
        width.append([i * 1 / group_number, (i + 1) / group_number])
    group_long_yield = []
    for i in range(len(width)):
        temp = calculate_yield(
            factor=factor,
            yield_matrix=yield_matrix,
            low_limit=width[i][0],
            high_limit=width[i][1],
            stocks=0,
            holding_periods=holding_periods,
            method='long'
        )
        group_long_yield.append({'cumu': temp['yield']['cumu'], 'not_cumu': temp['yield']['not_cumu']})
        print('第%d组分档多头净值序列计算完毕！' % (i+1))
    return group_long_yield
