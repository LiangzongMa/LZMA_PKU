# 设计运算符号的函数
# 注：被调用的数据来源都是numpy数组或者浮点数、整数
# 传入参数：x为前操作数，y为后操作数，C为运算符
import numpy as np
import warnings
import pandas as pd
import statsmodels.api as sm
warnings.filterwarnings("ignore")

def Calc(x, y, C, FileName):
    if isinstance(x, str):
        x = FileName[x]
    if isinstance(y, str):
        y = FileName[y]
########################################################################################################################

    '''对第一个操作数获取早上的数据，有意义的情况：
    1. 第一个操作数x为一个宽度为48的数组
    否则返回第一个操作数'''
    if C == 'GetMorning':
        if isinstance(x, np.ndarray) and x[0].shape[0] == 48:
            return x[:, 0:24, :]
        else:
            return x

    '''对第一个操作数获取下午的数据，有意义的情况：
        1. 第一个操作数x为一个宽度为48的数组
        否则返回第一个操作数'''
    if C == 'GetAfternoon':
        if isinstance(x, np.ndarray) and x[0].shape[0] == 48:
            return x[:, 24:48, :]
        else:
            return x

    '''计算整体加法，加法有意义的有如下情况：
    1. 两个维度相同的数组相加
    2. 两个数相加
    3. 一个数组和一个数相加
    如果不满足以上三种情况，返回第一个操作数'''
    if C == 'Add':
        try:
            result = x + y
        except:
            return x
        else:
            return result

    '''计算整体减法，整体减法有意义的有如下情况：
    1. 两个维度相同的数组相减
    2. 两个数相减
    3. 一个数组和一个数相减
    如果不满足以上三种情况，返回第一个操作数'''
    if C == 'Sub':
        try:
            result = x - y
        except:
            return x
        else:
            return result

    '''整体乘法，有以下有意义情况：
    1. 两个形状相同的数组的乘法
    2. 一个宽度大于1，一个宽度为1的数组的乘法
    3. 一个数组和一个数的乘法
    4. 两个数的乘法
    否则返回第一个操作数的值'''
    if C == 'Mul':
        try:
            result = x * y
        except:
            return x
        else:
            return result

    '''整体除法，有以下有意义情况：
        1. 两个形状相同的数组的除法
        2. 一个宽度大于1，一个宽度为1的数组的除法
        3. 一个数组和一个数的除法
        4. 两个数的除法
        否则返回第一个操作数的值'''
    if C == 'Div':
        try:
            result = x / y
            if isinstance(result, np.ndarray):
                result[np.isinf(result)] = np.nan
            else:
                if np.isinf(result):
                    result = np.nan
        except:
            return x
        else:
            return result

    '''两个数组相关系数计算，以下为有意义情况：
    1. 两个数组宽度与长度均相同
    否则返回第一个操作数x'''
    if C == 'Corr':
        if isinstance(x, np.ndarray) and isinstance(y, np.ndarray) \
                and x.shape[1] == y.shape[1] and x.shape[2] == y.shape[2]:
            mid = []
            for i in range(len(x)):
                X = x[i]
                X1 = X - np.nanmean(X, axis=0)
                Y = y[i]
                Y1 = Y - np.nanmean(Y, axis=0)
                XY = X1 * Y1
                XY = np.nanmean(XY, axis=0)
                XStd = np.nanstd(X, axis=0)
                YStd = np.nanstd(Y, axis=0)
                result = XY / (XStd * YStd)
                mid.append(result)
            Result = np.array(mid).reshape(x.shape[0], 1, x.shape[2])
            return Result
        else:
            return x

    '''获取第一个操作数每一天的每一支股票所有5min线的平均值，以下为有意义的情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetMean':
        if isinstance(x, np.ndarray):
            return np.nanmean(x, axis=1).reshape(x.shape[0], 1, x.shape[2])
        else:
            return x

    '''获取每个横截面的均值，以下为有意义情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetCrossMean':
        try:
            result = np.nanmean(x, axis=2).reshape(x.shape[0], x.reshape[1], 1)
        except:
            return x
        else:
            return result

    '''获取第一个操作数每一天的每一支股票所有5min线的最大值，以下为有意义的情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetMax':
        if isinstance(x, np.ndarray):
            return np.nanmax(x, axis=1).reshape(x.shape[0], 1, x.shape[2])
        else:
            return x

    '''获取第一个操作数每一天的每一支股票所有5min线的最小值，以下为有意义的情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetMin':
        if isinstance(x, np.ndarray):
            return np.nanmin(x, axis=1).reshape(x.shape[0], 1, x.shape[2])
        else:
            return x

    '''获取每一天每一个股票的第一行线的数据，以下为有意义的情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetStart':
        if isinstance(x, np.ndarray):
            return x[:, 0, :].reshape(x.shape[0], 1, x.shape[2])
        else:
            return x

    '''获取每一天每一个股票的最后一行线数据，以下为有意义的情况：
    1. 第一个操作数为一个数组
    否则返回第一个操作数'''
    if C == 'GetLast':
        if isinstance(x, np.ndarray):
            return x[:, x.shape[1] - 1, :].reshape(x.shape[0], 1, x.shape[2])
        else:
            return x

    '''获取每一天每一个股票的所有行的标准差，以下为有意义的情况：
    1. 第一个操作数是一个数组
    否则返回第一个操作数'''
    if C == 'GetStd':
        if isinstance(x, np.ndarray):
            result = np.nanstd(x, axis=1).reshape(x.shape[0], 1, x.shape[2])
            return result
        else:
            return x

    '''对第一个操作数取对数，以下为有意义的情况:
    1. 第一个操作数是一个矩阵，矩阵中的元素大于0
    2. 第一个操作数是一个常数，则此常数大于0
    否则第一种情况对应的位置命名为nan，第二种情况直接返回第一个操作常数'''
    if C == 'Log':
        if isinstance(x, np.ndarray):
            x[x <= 0] = np.nan
            return np.log(x)
        elif x <= 0:
            return x
        else:
            return np.log(x)

    '''对第一个操作数的每一根k线对过去5根加权，权重为0.8的指数次方，以下为有意义情况：
    1. 第一个操作数是一个矩阵，且第二维度大于等于5
    否则返回第一个操作数'''
    if C == 'Weight_5_8':
        try:
            x_new = x
            if x.shape[1] >= 5:
                Weight = 0.8 ** np.array([4, 3, 2, 1, 0] * x.shape[2]).reshape(5, x.shape[2])
                x_new = np.array([np.nan] * x.shape[0] * (x.shape[1] - 4) * x.shape[2]).reshape(x.shape[0],
                                                                                                x.shape[1] - 4,
                                                                                                x.shape[2])
                for i in range(x.shape[0]):
                    for j in range(4, x.shape[1]):
                        x_new[i, j - 4, :] = x[i, j - 4:j + 1, :].dot(Weight) / np.nansum(Weight)
        except:
            return x
        else:
            return x_new

    '''取差分，以下为有意义情况：
    1. 第一个操作数为一个矩阵
    否则返回第一个操作数'''
    if C == 'Diff':
        if isinstance(x, np.ndarray) and x.shape[1] >= 2:
            try:
                result = x[:, 1:x.shape[1], :] - x[:, 0:x.shape[1] - 1, :]
            except:
                return x
            else:
                return result
        else:
            return x

    '''去除第一个操作数第二维度的第一根线（此函数作用为配合一些其他函数的运算），以下为有意义情况：
    1. 第一个操作数为一个矩阵，第二维度大于等于2
    否则返回第一个操作数'''
    if C == 'RemoveFirst':
        try:
            if x.shape[1] >= 2:
                result = x[:, 1:x.shape[1], :]
            else:
                result = x
        except:
            return x
        else:
            return result

    '''对x和y在第二维度上的每一列数据进行对应的无截距回归，x为被解释变量，y为解释变量，以下为有意义的情况：
    1. x和y的对应维度可以进行无截距回归操作（若有数据缺失则为nan）
    否则返回第一个操作数'''
    if C == 'OLS_NoConstant':
        try:
            result = []
            for i in range(x.shape[0]):
                Y = x[i]
                X = y[i]
                mid = np.nansum(X * Y, axis=0) / np.nansum(X ** 2, axis=0)
                result.append(mid)
            result = np.array(result).reshape(x.shape[0], 1, x.shape[2])
        except:
            return x
        else:
            return result

    '''计算第一个操作数x的第二维度方向上的增长率，以下为有意义的情况：
    1. 第一个操作数x第二维度大于等于2
    否则返回第一个操作数'''
    if C == 'GrowthRate':
        try:
            if x.shape[1] >= 2:
                result = (x[:, 1:x.shape[1], :] - x[:, 0:x.shape[1] - 1, :]) / np.abs(x[:, 0:x.shape[1] - 1, :])
                result[np.isinf(result)] = np.nan
            else:
                result = x
        except:
            return x
        else:
            return result

    '''对第三维度方向取均值（衡量市场程度），以下为有意义的情况：
    1. 第一个操作数为一个矩阵'''
    if C == 'GetMeanMarket':
        try:
            result = []
            for i in range(0, x.shape[0]):
                for j in range(0, x.shape[1]):
                    result.append(np.nanmean(x[i, j, :]))
            x = np.array(result).reshape(x.shape[0], x.shape[1], 1)
        except:
            return x
        else:
            return x

    '''寻找大于0的市场情况，以下为有意义的情况：
    1. 为一个三维矩阵，第三维度为1
    否则返回第一个操作数'''
    if C == 'GetMarket_OverZero':
        try:
            if x.shape[2] == 1:
                return x > 0
            else:
                return x
        except:
            return x

    '''寻找小于0的市场情况，以下为有意义的情况：
    1. 为一个三维矩阵，第三维度为1
        否则返回第一个操作数'''
    if C == 'GetMarket_BelowZero':
        try:
            if x.shape[2] == 1:
                return x < 0
            else:
                return x
        except:
            return x

    '''对第一个操作数取切片，以下为有意义的情况：
    1. 第一个操作数为一个三维矩阵
    2. 第二个操作数为一个三维矩阵，第三维长度为1，且所有数据均为0或1（False或者True）（这个数据是用来表示市场状况的）'''
    if C == 'GetSlice':
        if isinstance(y, np.ndarray) and y.shape[2] == 1:
            flag = 1
            for i in range(y.shape[0]):
                for j in range(y.shape[1]):
                    if y[i, j, 0] not in [0, 1]:
                        flag = 0
                        break
                if flag == 0:
                    return x
            try:
                result = x.copy()
                for i in range(x.shape[0]):
                    for j in range(x.shape[1]):
                        if y[i, j, 0] == 0:
                            result[i, j, :] = np.nan
            except:
                return x
            else:
                return result
        else:
            return x

    '''对x和y进行连接，仅在第三维上进行连接，要求y在第三维的维度为1，以下为有意义的情况：
    1. 第一个操作数为一个三维矩阵
    2. 第二个操作数为一个三维矩阵，第三维维度为1
    3. 第一个和第二个操作数的第一第二维度相同
    否则返回第一个操作数'''
    if C == 'Link_Single':
        if isinstance(x, np.ndarray) and isinstance(y, np.ndarray) and y.shape[2] == 1:
            if x.shape[0] == y.shape[0] and x.shape[1] == y.shape[1]:
                result = np.array([np.nan] * x.shape[0] * x.shape[1] * (x.shape[2] + y.shape[2])).reshape\
                    (x.shape[0], x.shape[1], (x.shape[2]+y.shape[2]))
                for i in range(x.shape[0]):
                    result[i] = np.hstack((x[i], y[i]))
                return result
            else:
                return x
        else:
            return x

    '''对第一个操作数的第三维度取方差，以下为有意义的情况：
    1. 第一个操作数为一个矩阵
    否则返回第一个操作数'''
    if C == 'Variance':
        try:
            result = []
            for i in range(x.shape[0]):
                for j in range(x.shape[2]):
                    result.append(np.var(x[i, :, j]))
            result = np.array(result).reshape(x.shape[0], 1, x.shape[2])
            return result
        except:
            return x

    '''对第一个操作数和第二个操作数取协方差，要求第二个操作数的第三维度为1维，以下为有意义的情况：
    1. 第一个操作数为一个矩阵，且第一维和第二维和第二个操作数的维度相同
    2. 第二个操作数的第三维度为1
    否则返回第一个操作数'''
    if C == 'Cov_Single':
        try:
            if y.shape[2] == 1:
                try:
                    result = []
                    for i in range(x.shape[0]):
                        for j in range(x.shape[2]):
                            result.append(np.cov(x[i, j], y[i]))
                    result = np.array(result).reshape(x.shape[0], 1, x.shape[2])
                    return result
                except:
                    return x
            else:
                return x
        except:
            return x
