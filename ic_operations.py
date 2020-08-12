# ic计算与与ic有关的衍生变量的计算
# 主要包括ic的计算与ic衰减的计算

import numpy as np
import bottleneck as bn
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

def ic_calculate(factor, yield_matrix, periods=1, method='spearman'):
    """
    按照期限为periods来计算IC

    Parameters
    ----------
    factor：因子的数据矩阵(pd.DataFrame)
    yield_matrix：股票收益率矩阵(pd.DataFrame)
    periods：期限
    method：'spearman'或者'pearson'，表示使用对应的方法计算IC

    Returns
    -------
    -1：表示传入的计算方法非spearman或者pearson
    计算得到的IC序列，为pd.Series形式

    Notes
    -------
    在计算IC的时候应当注意：由于此回测程序是为了做自己的研究，所以只有在当天收盘后，才可以得到当天的数据，此数据应当用于明天的投
    资，所以计算时候应当用T期的因子值与T+1期到T+2期的收益率来计算IC
    """

    index = factor.index
    factor_numpy = np.array(factor)
    ret_numpy = np.array(yield_matrix)

    periods += 1  # 这样处理的原因可以参考函数说明中的 Notes 部分

    # 对齐
    ret_numpy[0:ret_numpy.shape[0] - periods] = ret_numpy[periods:ret_numpy.shape[0]]
    ret_numpy[ret_numpy.shape[0] - periods:ret_numpy.shape[0]] = np.nan

    # 空值对应
    factor_numpy[np.isnan(ret_numpy)] = np.nan
    ret_numpy[np.isnan(factor_numpy)] = np.nan

    if method == 'spearman':
        nan_matrix = np.isnan(factor_numpy)
        factor_numpy = bn.rankdata(factor_numpy, axis=1)
        ret_numpy = bn.rankdata(ret_numpy, axis=1)
        factor_numpy[nan_matrix] = np.nan
        ret_numpy[nan_matrix] = np.nan
    elif method == 'pearson':
        pass
    else:
        print('指定计算方法错误！')
        return -1

    ic_temp = np.nanmean(factor_numpy * ret_numpy, axis=1) - np.nanmean(factor_numpy, axis=1) * np.nanmean(ret_numpy, axis=1)
    ic = ic_temp / (np.nanstd(factor_numpy, axis=1) * np.nanstd(ret_numpy, axis=1))
    ic = pd.Series(ic, index=index)
    return ic


def ic_decrease(factor, yield_matrix, periods=10):
    """
    计算IC衰减

    Parameters
    ----------
    factor：因子矩阵(pd.DataFrame格式)
    yield_matrix：收益率矩阵(pd.DataFrame格式)
    periods：计算IC衰减考察的时间跨度

    Returns
    -------
    pd.DataFrame，columns为1-periods，每一列表示对应的IC序列

    Notes
    -------
    IC衰减牵涉到IC的计算，在计算IC的时候应当注意：由于此回测程序是为了做自己的研究，所以只有在当天收盘后，才可以得到当天的数据，
    此数据应当用于明天的投资，所以计算时候应当用T期的因子值与T+1期到T+2期的收益率来计算IC
    """
    ret = pd.DataFrame(columns=np.arange(periods)+1, index=factor.index)
    for i in range(periods):
        ret[i+1] = ic_calculate(factor, yield_matrix, periods=i+1)
    return ret



