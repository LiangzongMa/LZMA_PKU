# 进行初始数据规整的函数，生成未经过权处理的结果
import numpy as np
import scipy.io as sio
import os
import time


'''数据规整函数，传入部分为三个参数，规整的数据名称，频率，起始日期'''


def DataHandling(FactorName, Frequency, StartDate, Path):
    os.chdir(Path)
    TradeDate = sio.loadmat("StockTradeDate.mat")['StockTradeDate']
    EndDate = TradeDate[len(TradeDate)-1][0]
    Time_Start = time.time()
    os.chdir(Path+'/'+FactorName)
    FileName = os.listdir(Path+'/'+FactorName)
    FileName_Copy = []
    for i in range(len(FileName)):
        Date = int(FileName[i].split('.')[0].split('_')[1])
        if Date >= StartDate and Date <= EndDate:
            FileName_Copy.append(FileName[i])
    FileName = FileName_Copy
    # 对FileName按照日期排序
    i = len(FileName) - 1
    while i > 0:
        flag = 1
        j = 0
        while j < i:
            if int(FileName[j].split('_')[1].split('.')[0]) > int(FileName[j + 1].split('_')[1].split('.')[0]):
                    mid = FileName[j]
                    FileName[j] = FileName[j + 1]
                    FileName[j + 1] = mid
                    flag = 0
            j += 1
        if flag:
            break
        i = i - 1
    # 按照给定的频率生成数组
    i = 0
    LastData = sio.loadmat(FileName[len(FileName)-1])[FileName[len(FileName)-1].split('.')[0]]
    StockNumber = LastData.shape[1]
    FinalData = []
    while i < len(FileName):
        start_time = time.time()
        DataMid = sio.loadmat(FileName[i])[FileName[i].split('.')[0]]
        if DataMid.shape[1] < StockNumber:
            for j in range(StockNumber-DataMid.shape[1]):
                NaN = [np.nan] * 48
                DataMid = np.column_stack((DataMid, np.array(NaN)))
        FinalData.append(DataMid)
        print(FileName[i]+'转换完毕')
        end_time = time.time()
        print('用时：', end_time-start_time, 's\n')
        i += Frequency
    FinalData = np.array(FinalData)
    Time_End = time.time()
    print('数据已全部转换完毕，形状为：', FinalData.shape)
    print('用时：', Time_End-Time_Start, 's\n\n')
    os.chdir(Path)
    np.save(FactorName+'_'+str(StartDate)+'_'+str(EndDate)+'_'+str(Frequency)+'Day.npy', FinalData)


if __name__ == '__main__':
    Path = ''
    FactorName = 'StockOpen5M'
    Frequency = 5
    StartDate = 20160105
    DataHandling(FactorName, Frequency, StartDate, Path)













