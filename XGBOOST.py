# 基于所选出的因子做XGBOOST模型
# 对过去的20个交易日的收益预测取均值作为因子值


import xgboost as xg
import pandas as pd
import numpy as np
import time
import warnings
warnings.filterwarnings('ignore')

START = time.time()
# 声明调仓周期
holding_periods = 2

# 导入数据
print('正在导入数据...')
open_price = pd.read_csv('open.csv', index_col='date', parse_dates=['date'])
factor_collection = ['003', '006', '011', '016', '017', '029', '030', '031', '034', '041', '074']
for i in range(len(factor_collection)):
    start_time = time.time()
    print('正在导入因子...')
    factor_collection[i] = pd.read_csv('factor_TongDao_Alpha_'+factor_collection[i]+'.csv', parse_dates=['date'], index_col='date').values
    end_time = time.time()
    print('第%d个因子导入完毕，用时：%.2f秒' % (i+1, end_time-start_time))
ret = np.array([np.nan] * open_price.shape[0] * open_price.shape[1]).reshape(open_price.shape[0], open_price.shape[1])
yield_rate = open_price.pct_change(periods=holding_periods).values
print('数据导入完毕！\n')

# 对因子值与收益率做标准化
print('正在进行数据的进一步处理...')
for i in range(len(factor_collection)):
    factor_collection[i] = (factor_collection[i] - np.nanmean(factor_collection[i], axis=1).reshape(open_price.shape[0], 1)) / np.nanstd(factor_collection[i], axis=1).reshape(open_price.shape[0], 1)
yield_rate = (yield_rate - np.nanmean(yield_rate, axis=1).reshape(open_price.shape[0], 1)) / np.nanstd(yield_rate, axis=1).reshape(open_price.shape[0], 1)
# 对空值做处理
yield_rate[np.isnan(yield_rate)] = 0
for i in range(len(factor_collection)):
    factor_collection[i][np.isnan(factor_collection[i])] = 0

# 构建模型
print('\n正在构建模型...')
days = list(np.arange(20))
for i in range(ret.shape[0]):
    start_time = time.time()
    temp = np.array([np.nan] * len(days) * open_price.shape[1]).reshape(len(days), open_price.shape[1])
    if i <= days[-1] + holding_periods:
        end_time = time.time()
        print('第%d次循环处理完毕，用时：%.2f秒' % (i + 1, end_time - start_time))
        continue
    # 先构造每次都要使用的测试集
    x_test = np.array([np.nan] * len(factor_collection) * open_price.shape[1]).reshape(open_price.shape[1], len(factor_collection))
    for j in range(len(factor_collection)):
        x_test[:, j] = factor_collection[j][i].T
    for j in days:
        y = yield_rate[i-j]
        x = np.array([np.nan] * len(factor_collection) * open_price.shape[1]).reshape(open_price.shape[1], len(factor_collection))
        for k in range(len(factor_collection)):
            x[:, k] = factor_collection[k][i-j-holding_periods-1].T
        model = xg.XGBRegressor()
        model.fit(x, y)
        temp[j, :] = model.predict(x_test)
    ret[i] = np.nanmean(temp, axis=0)
    end_time = time.time()
    print('第%d次循环处理完毕，用时：%.2f秒' % (i+1, end_time - start_time))
ret = pd.DataFrame(ret, columns=open_price.columns, index=open_price.index)
ret.to_csv('XGBOOST.csv')

END = time.time()
print('数据生成过程结束，用时：%.2f秒\n' % (END - START))
