import time
import numpy as np


'''设置遗传规划需要的基础参数'''
def BasicGPDataSet():
    # 初始生成树数量控制
    TREENUMBER = [20, 30]
    # 公式大致长度控制
    Lenth = 30
    # 遗传代数
    Generation = 2
    # 存活率
    DieRate = 0.5
    return TREENUMBER, Lenth, Generation, DieRate


'''设置希望引入主函数的参数'''
def BasicDataSet():
    # 希望引入的数据集
    Data = ['ClosePrice5M_5Day', 'OpenPrice5M_5Day', 'HighPrice5M_5Day', 'LowPrice5M_5Day', 'RealVolume5M_5Day',
            'StockAmount5M_5Day', 'FreeFloatShare_20160105_20191022_5Day']
    # 希望添加的常数
    ScalarData = [2, 3, 5]
    TotalData = Data + ScalarData
    # 希望引入的运算符
    Charactor = ['GetMorning', 'GetAfternoon', 'Add', 'Sub', 'Mul', 'Div', 'Corr', 'GetMean', 'GetMax', 'GetStart',
                 'GetLast', 'GetStd', 'Log', 'Weight_5_8', 'Diff', 'RemoveFirst', 'GrowthRate', 'GetMeanMarket',
                 'GetMarket_OverZero', 'GetMarket_BelowZero', 'GetSlice', 'Link_Single', 'Variance', 'Cov_Single', 'OLS_NoConstant']

    FileName = {}
    print("准备导入数据库中的数据")
    for i in Data:
        start_time = time.time()
        FileName[i] = np.load(i + '.npy')
        end_time = time.time()
        print("导入%s数据完毕，用时：%.2f" % (i, end_time - start_time), '秒')

    return FileName, TotalData, Charactor

    '''每次仅仅修改上述三个#号上的参数即可'''


