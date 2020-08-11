# 权重处理模块，生成需要的数据格式的权
import os
import numpy as np
import scipy.io as sio
import time
def DataHandling_Factor(Path, StandardName, Name, StartDate, Frequency):
    S = time.time()
    os.chdir(Path)
    NameFactor = sio.loadmat(Name)[Name.split('.')[0]]
    TradeDate = sio.loadmat('StockTradeDate.mat')['StockTradeDate']
    EndDate = TradeDate[len(TradeDate)-1][0]
    TradeDate = TradeDate.reshape(len(TradeDate))
    StandardName = np.load(StandardName)
    NameFactor = NameFactor[TradeDate >= StartDate]
    NewNameFactor = []
    i = 0
    while i < len(NameFactor):
        start_time = time.time()
        mid = NameFactor[i].reshape(1, len(NameFactor[i]))
        for j in range(StandardName.shape[2] - mid.shape[1]):
            mid = np.column_stack((mid, np.nan))
        for j in range(StandardName.shape[1]-1):
            mid = np.row_stack((mid, mid[0]))
        print("第%d行处理结束" % (i+1))
        end_time = time.time()
        print("用时：", end_time-start_time, '秒\n')
        NewNameFactor.append(mid)
        i = i + Frequency
    NewNameFactor = np.array(NewNameFactor)
    E = time.time()
    print("数据已全部处理完毕，用时：", E - S, '秒')
    print("形状为：", NewNameFactor.shape)
    np.save(Name.split('.')[0] + '_' + str(StartDate) + '_' + str(EndDate) + '_' + str(Frequency) + "Day.npy", NewNameFactor)


if __name__ == '__main__':
    Path = '/Users/littlelion/Desktop/遗传规划/DataBase'
    Name = 'FreeFloatShare.mat'
    Frequency = 5
    DataHandling_Factor(Path, 'StockOpen5M_20160105_20191022_5Day.npy', Name, 20160105, Frequency)



