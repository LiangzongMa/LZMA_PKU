# 设计计算适应度的函数
import numpy as np
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

def CalcFitness(Factor, OpenPrice):

    Factor = np.nanmean(Factor, axis = 1)
    OpenPrice = OpenPrice[:, 0, :]
    IC = []
    for i in range(Factor.shape[0]-1):
        FactorValue = pd.Series(Factor[i])
        YieldRate = pd.Series((OpenPrice[(i+1)*5] - OpenPrice[i*5+1]) / np.abs(OpenPrice[i*5+1]))
        YieldRate[np.isinf(YieldRate)] = np.nan
        mid = FactorValue.corr(YieldRate)
        if np.isnan(mid):
            return np.nan
        else:
            IC.append(mid)
    IC = np.array(IC)
    return np.abs(np.nanmean(IC) / np.nanstd(IC))



