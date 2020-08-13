#!/usr/bin/env python
# coding: utf-8

# # 中证500指数增强

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')



# 导入数据
# 所有基金的基本信息
fund_info = pd.read_pickle('fund/fund_info')

# 所有基金的股票持仓明细
stock_portfolio = pd.read_pickle('fund/stock_portfolio')

# 所有个股的行业归属
indus_belong_init = pd.read_pickle('stock/indus_belong')
indus_belong = indus_belong_init.copy()

# 中证500成分股权重
zz500_weight = pd.read_pickle('index/zz500_weight')

# 中证500指数增强产品
zz500_products = list(pd.read_excel('ZZ500指数增强产品目录.xlsx')['基金代码'])

# 获得日期
date_collection = zz500_weight.index.to_list()


indus_belong = indus_belong.stack().reset_index()
indus_belong['indus'] = indus_belong[0]
del indus_belong[0]

indus_belong['报告期'] = indus_belong['date']
del indus_belong['date']
indus_belong['持有个股代码'] = indus_belong['stock_code']
del indus_belong['stock_code']



# 获取行业
indus_collection = list(indus_belong['indus'].unique())



# 获取中证500每个报告期的行业持比重
zz500_indus = pd.DataFrame(index=indus_collection, columns=date_collection)
for date in date_collection:
    temp = {}
    weight_ = (zz500_weight.loc[date, :] * (-pd.isna(indus_belong_init.loc[date, :]))).sum()
    for indus in indus_collection:
        temp[indus] = zz500_weight.loc[date, :].mul(indus_belong_init.loc[date, :]==indus).div(weight_).sum()
    zz500_indus.loc[:, date] = pd.Series(temp)


# 处理每个考察日期
date_data = {} # 储存基金集合的时间序列书序
single_data = {} # 储存单个基金的时间序列数据
for product in zz500_products:
    single_data[product] = []
for date in date_collection:
    print('正在处理：', date)
    if date.month == 3 or date.month == 9:
        print('非半年报或年报，跳过')
        continue
    temp = {}
    temp_weight = {}
    for product in zz500_products:
        try:
            port = stock_portfolio[stock_portfolio['基金代码'].isin([product])].set_index('报告期').loc[date, :] # 获取基金信息
            port['股票占基金净值比例'] = port['持有个股市值'].div(port['持有个股市值'].sum())
            port = pd.merge(port, indus_belong, on=['报告期', '持有个股代码'])
        except:
            pass
        else:
            indus_dic = {}
            weight_dic = {}
            for j in indus_collection:
                indus_dic[j] = np.sum(np.array(port['indus'] == j).astype(int) * np.array(port['股票占基金净值比例']))
                weight_dic[j] = np.sum(np.array(port['indus'] == j).astype(int)) / port.shape[0]
            temp[product] = indus_dic
            temp_weight[product] = weight_dic
    temp_ = {}
    for i in temp.keys():
        mid = pd.Series(temp[i])
        mid = mid.div(zz500_indus.loc[:, date]) - 1
        mid[np.isinf(mid)] = np.nan
        temp_[i] = mid
    add_ = pd.DataFrame(temp_)
    add_['average'] = add_.abs().mean(axis=1)
    weight_matrix = pd.DataFrame(temp_weight)
    product_average = add_.iloc[:, :-1].abs().mul(weight_matrix).sum(axis=0)
    product_average['average'] = np.nan
    product_average.name = 'product_average'
    if len(product_average) != 1:
        add_ = add_.append(product_average)
        for i in product_average.index[:-1]:
            single_data[i].append(add_.loc[add_.index[:-1], i])
    date_data[date] = add_
    print(date, '处理完毕')

keys = list(date_data.keys())

writer = pd.ExcelWriter('zz500_result.xlsx')

date_useful = []
for i in keys:
    if date_data[i].shape[0] != 0:
        date_data[i].to_excel(writer, sheet_name=i.strftime('%Y.%m.%d'))
        date_useful.append(i)
conclusion = pd.DataFrame(index=indus_collection, columns=date_useful)
for i in date_useful:
    conclusion.loc[:, i] = date_data[i]['average']
conclusion.to_excel(writer, sheet_name='conclusion')
for i in single_data.keys():
    temp = 0
    for j in range(len(single_data[i])):
        temp += single_data[i][j].abs()
    if len(single_data[i]) != 0:
        single_data[i] = temp / len(single_data[i])
    else:
        single_data[i] = pd.Series(index=indus_collection)
single_conclusion = pd.DataFrame(single_data)
single_conclusion.to_excel(writer, sheet_name='single_conclusion')
writer.save()

