# 因子导入，目目标指数导入与预处理
# 主要完成因子的截面去极值，截面标准化，市值中性化，行业中性化等等
# 还包括回测文件夹的建立等工作
import pandas as pd
import os


def load_data(factor_name,  index_name, start_date=None, end_date=None):
    """
    导入因子数据与目标指数数据，默认为csv格式

    Parameters
    ----------
    factor_name：导入因子的文件名（不包括文件后缀csv）
    start_date：要截取的数据开始日期，默认为None，表示不做截取
    end_date：要截取的数据结束日期，默认为None，表示不做截取
    index_name：导入目标指数的文件名（不包括文件后缀csv）

    Returns
    -------
    当返回-1时，说明数据格式部分不一致，发现错误
    返回一个字典
    传入factor_name可以得到因子的pd.DataFrame格式数据
    传入index_name可以得到指数的pd.DataFrame数据
    传入'open'可以得到收盘价数据

    Notes
    -------
    导入数据的部分会直接将收盘价收据导入，方便后续的其他操作
    """
    factor = pd.read_csv('factor_database/'+factor_name+'.csv', index_col='date', parse_dates=['date'])
    index = pd.read_csv('backtest_database/'+index_name+'.csv', index_col='date', parse_dates=['date'])
    # close = pd.read_csv('backtest_database/close.csv', index_col='date', parse_dates=['date']) 回测过程中一律使用开盘价计算
    open = pd.read_csv('backtest_database/open.csv', index_col='date', parse_dates=['date'])
    if start_date is not None:
        factor = factor[factor.index >= start_date]
        index = index[index.index >= start_date]
        # close = close[close.index >= start_date]
        open = open[open.index >= start_date]
    if end_date is not None:
        factor = factor[factor.index <= end_date]
        index = index[index.index <= end_date]
        # close = close[close.index <= end_date]
        open = open[open.index <= end_date]
    if factor.shape[0] != index.shape[0]:
        print('因子时间跨度与目标指数时间跨度不一致！')
        return -1
    if factor.shape != open.shape:
        print('因子形状与开盘价形状不一致！')
        return -1
    ret = {factor_name: factor, index_name: index, 'open': open}
    return ret


def winsorize_cross(factor, low_quantile, high_quantile):
    """
    因子横截面去极值：因子横截面上高于上限分位数的值都替换为上限分位数，低于下限分位数的值都替换为下限分位数

    Parameters
    ----------
    factor：因子数据，应当为pd.DataFrame格式
    low_quantile：横截面下限分位数
    high_quantile：横截面上限分位数

    Returns
    -------
    处理后的因子值
    """
    def cross_section(x):
        x_quantile = x.quantile([low_quantile, high_quantile])
        x[x >= x_quantile[high_quantile]] = x_quantile[high_quantile]
        x[x <= x_quantile[low_quantile]] = x_quantile[low_quantile]
        return x
    factor = factor.apply(cross_section, axis=1)
    return factor

def standardize_cross(factor):
    """
    因子横截面标准化

    Returns
    -------

    """
    factor = factor.sub(factor.mean(axis=1, skipna=True), axis=0).div(factor.std(axis=1, skipna=True), axis=0)
    return factor

def size_neutralize(factor):
    """
    市值中性化

    Returns
    -------

    """
    return factor

def industry_neutralize(factor):
    """
    行业中性化

    Returns
    -------

    """
    return factor

def create_result_file(factor_name):
    """
    创建回测结果中的因子回测结果文件夹

    Returns
    -------

    """
    print('正在创建因子回测结果文件夹...')
    try:
        os.mkdir('backtest_result/'+factor_name)
    except:
        print('因子回测结果文件夹已经存在')
    print('创建完毕！\n')










