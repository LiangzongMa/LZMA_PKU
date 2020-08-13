# 设计计算适应度的函数
import numpy as np
import warnings
import pandas as pd
warnings.filterwarnings("ignore")


def CalcFitness(Factor, OpenPrice):
    YieldRate = pd.DataFrame(OpenPrice).pct_change(periods=1)
    Factor = pd.DataFrame(Factor)
    YieldRate = YieldRate.iloc[2:]
    Factor = Factor.iloc[:-2]
    ic_temp = YieldRate.mul(Factor).mean(axis=1) - YieldRate.mean(axis=1) * Factor.mean(axis=1)
    ic = ic_temp.div(Factor.std(axis=1)).div(YieldRate.std(axis=1))
    if ic。std() != 0:
        return np.abs(ic.mean() / ic.std())
    else:
        return np.nan



