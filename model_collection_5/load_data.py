import time
import scipy.io as sio
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

START_TIME = time.time()

print('数据预处理开始运行...\n')

print('正在导入数据...')
start_time = time.time()
industry = sio.loadmat('StockZx.mat')['StockZx']   #表示29个行业
end_time = time.time()
print('StockZx导入完毕，累计用时：%.2f秒' % (end_time - start_time))

stock_close = sio.loadmat('StockClose.mat')['StockClose']   #收盘价
end_time = time.time()
print('StockClose导入完毕，累计用时：%.2f秒' % (end_time - start_time))    

stock_factor = sio.loadmat('StockFactor.mat')['StockFactor']   #前复权因子（使用时候需要收盘价与复权因子相乘来作为真正的收盘价）
end_time = time.time()
print('StockFactor导入完毕，累计用时：%.2f秒' % (end_time - start_time))

stock_tradedate = sio.loadmat('StockTradeDate.mat')['StockTradeDate']  #股票交易的日期
end_time = time.time()
print('StockTradeDate导入完毕，累计用时：%.2f秒' % (end_time - start_time))

stock_stop = sio.loadmat('StockStop.mat')['StockStop']  #股票是否停牌，如果为1表示停牌了
stock_stop = stock_stop[0:stock_stop.shape[0] - 1]  #多了一天所以截去
end_time = time.time()
print('StockStop导入完毕，累计用时： %.2f秒' % (end_time - start_time))

stock_st = sio.loadmat('StockSt.mat')['StockSt']   #判断股票是否异常，如果为1则表示异常，为nan则表示非异常
stock_st = stock_st[0:stock_st.shape[0] - 1]  #多了一天所以截去
end_time = time.time()
print('StockSt导入完毕，累计用时： %.2f秒' % (end_time - start_time))

stock_trade_day_count = sio.loadmat('StockTradeDayCount.mat')['StockTradeDayCount']   #股票交易了多久
end_time = time.time()
print('StockTradeDayCount导入完毕，累计用时： %.2f秒' % (end_time - start_time))

close_price = stock_close * stock_factor   #真正收盘价

risk_beta = sio.loadmat('Risk_Beta.mat')['Risk_Beta']  #1
end_time = time.time()
print('Risk_Beta导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_btop = sio.loadmat('Risk_BTOP.mat')['Risk_BTOP']  #2
end_time = time.time()
print('Risk_BTOP导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_earnings_yield = sio.loadmat('Risk_EarningsYield.mat')['Risk_EarningsYield']  #3
end_time = time.time()
print('Risk_EarningsYield导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_growth = sio.loadmat('Risk_Growth.mat')['Risk_Growth']  #4
end_time = time.time()
print('Risk_Growth导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_leverage = sio.loadmat('Risk_Leverage.mat')['Risk_Leverage']  #5
end_time = time.time()
print('Risk_Leverage导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_liquidity = sio.loadmat('Risk_Liquidity.mat')['Risk_Liquidity']  #6
end_time = time.time()
print('Risk_Liquidity导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_momentum = sio.loadmat('Risk_Momentum.mat')['Risk_Momentum']  #7
end_time = time.time()
print('Risk_Momentum导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_nonsize = sio.loadmat('Risk_NonSize.mat')['Risk_NonSize']  #8
end_time = time.time()
print('Risk_NonSize导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_residual_volatility = sio.loadmat('Risk_ResidualVolatility.mat')['Risk_ResidualVolatility']  #9 
end_time = time.time()
print('Risk_ResidualVolatility导入完毕，累计用时：%.2f秒' % (end_time - start_time))

risk_size = sio.loadmat('Risk_Size.mat')['Risk_Size']  #10
end_time = time.time()
print('Risk_Size导入完毕，累计用时：%.2f秒' % (end_time - start_time))

stock_list = sio.loadmat('StockList.mat')['StockList']  #股票代码列表，有3800个
end_time = time.time()
print('StockList.mat导入完毕，累计用时：%.2f秒' % (end_time - start_time))

new_judge_temp = pd.Series(list(stock_list)).apply(lambda x: x[0] == '3')
new_judge = np.array(list(new_judge_temp) * close_price.shape[0]).reshape(close_price.shape[0], close_price.shape[1]).astype(int)

end_time = time.time()
print("全部数据导入完毕，累计用时：%.2f秒\n" % (end_time - start_time))

print('正在对数据做进一步处理...')

# 截面标准化
barra_risk_factor = [risk_beta, risk_btop, risk_earnings_yield, risk_growth, risk_leverage,
                     risk_liquidity, risk_momentum, risk_nonsize,risk_residual_volatility,
                     risk_size]
for i in range(len(barra_risk_factor)):
    temp = barra_risk_factor[i] - np.nanmean(barra_risk_factor[i], axis=1).reshape(barra_risk_factor[i].shape[0], 1)
    barra_risk_factor[i] = temp / np.nanstd(barra_risk_factor[i], axis=1).reshape(barra_risk_factor[i].shape[0], 1)

'''特殊股票处理'''
start_time = time.time()
for i in range(len(barra_risk_factor)):
    barra_risk_factor[i][stock_st == 1] = np.nan
    barra_risk_factor[i][stock_stop == 1] = np.nan
    barra_risk_factor[i][stock_trade_day_count <= 120] = np.nan
    barra_risk_factor[i][np.isnan(barra_risk_factor[i])] = 0
end_time = time.time()
print('Barra风险因子截面标准化处理完毕，用时：%.2f秒' % (end_time - start_time))

risk_factor = barra_risk_factor + [industry] + [new_judge]

start_time = time.time()
returns = pd.DataFrame(close_price).pct_change(periods=1, axis=0).values
returns_temp = returns - np.nanmean(returns, axis=1).reshape(returns.shape[0], 1)
returns = returns_temp / np.nanstd(returns, axis=1).reshape(returns.shape[0], 1)
returns[np.isnan(returns)] = 0
end_time = time.time()
print('收益率计算并截面标准化完毕，用时：%.2f秒' % (end_time - start_time))

END_TIME = time.time()
print('\n数据全部处理完毕！')
print('用时：%.2f秒' % (END_TIME - START_TIME))
print('\n')