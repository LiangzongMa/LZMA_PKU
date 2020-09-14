import pandas as pd
import numpy as np
import datetime
import os

data_origin_file = os.listdir('部分宏观指标数据库')
data_origin = {}
for file in data_origin_file:
    try:
        data_temp = pd.read_excel('部分宏观指标数据库/'+file)
        frequency = data_temp.iloc[0, 1]
        data_temp = data_temp.iloc[1:data_temp.shape[0]-2]
        data_temp['date'] = data_temp['指标名称']
        del data_temp['指标名称']
    except:
        continue
    else:
        data_origin[file[:-5]] = {'data': data_temp, 'frequency': frequency}

file_name = list(data_origin.keys())

# 转化为月度数据
print('正在转化为月度数据...')
data_monthly = {} # 存放月度数据的字典
for file in file_name:
    if data_origin[file]['frequency'] != '年':
        data = data_origin[file]['data'].copy()
        if data_origin[file]['frequency'] != '月':
            data['date'] = data['date'].apply(lambda x: datetime.datetime.strptime(x[:-3], '%Y-%m'))
            data.iloc[:, 0] = data.iloc[:, 0].astype(float)
            data_monthly[file] = data.groupby('date').mean()
        else:
            data['date'] = data['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m'))
            data = data.set_index('date').astype(float)
            data_monthly[file] = data
print('月度数据转化完毕！\n')

# 计算月度环比
print('正在计算月度环比...')
data_mom = {} # 存放月度环比数据的字典
for file in data_monthly.keys():
    data_mom[file] = data_monthly[file].pct_change(periods=1)
print('月度环比计算完毕！\n')

# 计算月度同比
print('正在计算月度同比...')
data_yoy = {} # 存放月度同比数据的字典
for file in data_monthly.keys():
    data_ = data_monthly[file].copy()
    data_ = data_.resample('M').mean()
    if '率' in data_.columns[0]:
        data_ = data_.diff(periods=12)
    else:
        data_ = data_.pct_change(periods=12)
    data_yoy[file] = data_
print('月度同比计算完毕！\n')

# 筛选日期
for file in data_monthly.keys():
    data_monthly[file] = data_monthly[file].loc[data_monthly[file].index>='2000-01-01']
    data_mom[file] = data_mom[file].loc[data_mom[file].index>='2000-01-01']
    data_yoy[file] = data_yoy[file].loc[data_yoy[file].index>='2000-01-01']

# 存储数据
# 存储月度数据
print('正在储存数据...')
for file in data_monthly.keys():
    data_monthly[file].to_excel('部分宏观指标数据库-转化月度数据/'+file+'-月度.xlsx')
    data_mom[file].to_excel('部分宏观指标数据库-转化月度数据/'+file+'-月度环比.xlsx')
    data_yoy[file].to_excel('部分宏观指标数据库-转化月度数据/'+file+'-月度同比.xlsx')
print('数据储存完毕！')

print('\n\n程序运行结束.')

