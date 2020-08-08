# 建模思路：
# 首先用决策模型，利用行业因子与是否为创业板进行收益方向预测分类
# 再用回归模型使用10个Barra风险因子进行定量预测
# 当决策模型预测的方向与回归模型预测的符号相同时，则保留该值，如果相反，则设置为0
# 最后需要对收盘价为空值的位置做对应的赋值为空值的处理
import time

START_TIME = time.time()

from load_data import *
import xgboost as xg

factor = np.array([np.nan] * close_price.shape[0] * close_price.shape[1]).reshape(close_price.shape[0], close_price.shape[1])

days = list(range(21))

industry_nan_pos = []
for i in range(industry.shape[0]):
    industry_nan_pos.append(np.where(np.isnan(industry[i]))[0])

for i in range(factor.shape[0]):
    start_time = time.time()
    if i <= days[-1]:
        end_time = time.time()
        print('第%d次循环结束，用时：%.2f秒' % (i+1, end_time - start_time))
        continue

    '''决策模型'''
    judge_temp = np.array([np.nan] * close_price.shape[1] * len(days)).reshape(len(days), close_price.shape[1])
    for j in days:
        nan_pos = industry_nan_pos[i-j-1] # 该天行业因子为空的位置，为np.array一维数组
        y = np.delete(returns[i-j], nan_pos)
        y[y > 0] = 1
        y[y < 0] = -1
        x = industry[i-j-1]
        x = np.delete(x, nan_pos)
        x = x.reshape(-1, 1)
        if x.shape[1] != 0:
            model = xg.XGBClassifier()
            model.fit(x, y)
            x_test = industry[i]
            x_test = np.delete(x_test, industry_nan_pos[i])
            x_test = x_test.reshape(-1, 1)
            temp = model.predict(x_test)
            for k in industry_nan_pos[i]:
                temp = np.insert(temp, k, 0)
            judge_temp[j] = temp

    '''回归模型'''
    returns_temp = np.array([np.nan] * close_price.shape[1] * len(days)).reshape(len(days), close_price.shape[1])
    for j in days:
        y = returns[i-j]
        x = np.array([np.nan] * close_price.shape[1] * len(barra_risk_factor)).reshape(close_price.shape[1], len(barra_risk_factor))
        for k in range(len(barra_risk_factor)):
            x[:, k] = barra_risk_factor[k][i-j-1].T
        model = xg.XGBRegressor()
        model.fit(x, y)
        x_test = np.array([np.nan] * close_price.shape[1] * len(barra_risk_factor)).reshape(close_price.shape[1], len(barra_risk_factor))
        for k in range(len(barra_risk_factor)):
            x[:, k] = barra_risk_factor[k][i].T
        returns_temp[j] = model.predict(x_test)


    '''决策模型和回归模型比对'''
    temp = returns_temp / np.abs(returns_temp)
    judge_temp[judge_temp != temp] = 0
    judge_temp = np.abs(judge_temp)

    '''输出最终的预测'''
    factor[i] = np.mean(judge_temp * returns_temp, axis=0)
    end_time = time.time()
    print('第%d次循环结束，用时：%.2f秒' % (i + 1, end_time - start_time))

factor[np.isnan(close_price)] = np.nan
print('\n正在保存因子...')
sio.savemat('XGBOOST.mat', {'XGBOOST': factor})
print('因子保存完毕！')

END_TIME = time.time()
print('\n数据全部处理完毕！')
print('用时：%.2f秒' % (END_TIME - START_TIME))
print('\n')




