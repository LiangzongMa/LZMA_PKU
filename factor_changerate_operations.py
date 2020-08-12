# 计算因子换手率
import pandas as pd

def factor_change_rate(weight):
    """
    计算因子换手率

    Parameters
    ----------
    weight：0-1矩阵，0表示对应时间不持有该股票，1表示对应时间持有该股票

    Returns
    -------

    Notes
    -------
    采用股票数量变化计算换手率

    """
    weight = weight.fillna(0)
    weight[weight != 0] = 1
    weight_change = weight.diff(periods=1)
    stocks_change = (weight_change == -1).sum(axis=1)
    change_rate_temp = (weight == 1).sum(axis=1).shift(periods=1)
    change_rate = stocks_change / change_rate_temp
    return change_rate

