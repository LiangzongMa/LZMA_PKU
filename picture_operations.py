# 做图
# 主要为：分档净值曲线，分档柱状图，IC柱状图，IC衰减，多头/空头/多空组合收益曲线，因子换手率

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font",family='YouYuan')
import numpy as np
plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus'] = False

def picture(factor_name, group_yield_list, ic_series, holding_periods, ic_decrease_matrix, rev_dic, index_yield_dic, change_rate_series):
    """
    绘制有关图像

    Parameters
    ----------
    factor_name：因子名称
    group_yield_list：分档做多收益列表
    ic_series：ic序列
    ic_decrease_matrix：ic衰减矩阵
    rev_dic：多/空/多空组合收益字典
    index_yield_dic：基准收益字典

    Returns
    -------

    """
    fig = plt.figure(figsize=(64, 48))

    '''分档净值曲线'''
    group_yield_curve = fig.add_subplot(3, 2, 1)
    for i in range(len(group_yield_list)):
        group_yield_curve.plot(np.arange(len(group_yield_list[i]['cumu'])) + 1, group_yield_list[i]['cumu'], label=str(i + 1), linewidth=6)
    group_yield_curve.plot(
        np.arange(len(index_yield_dic['cumu'])) + 1,
        index_yield_dic['cumu'],
        label='基准',
        color='blue',
        linewidth=6)
    group_yield_curve.plot(
        np.arange(len(index_yield_dic['cumu'])) + 1,
        np.ones(len(index_yield_dic['cumu'])),
        color='black',
        linewidth=6)
    group_yield_curve.legend(loc='lower left', fontsize=40)
    plt.tick_params(labelsize=50)
    plt.title('分档收益序列曲线', fontsize=50)

    '''分档柱状图'''
    group_yield_bar = fig.add_subplot(3, 2, 2)
    group_yield_mean = []
    for i in range(len(group_yield_list)):
        group_yield_mean.append(np.mean(group_yield_list[i]['cumu']))
    group_yield_bar.bar(
        np.arange(len(group_yield_mean)) + 1,
        group_yield_mean,
        color='brown')
    group_yield_bar.plot(np.arange(len(group_yield_mean)) + 1,
                         [np.nanmean(index_yield_dic['cumu'])] * len(group_yield_mean),
                         label='基准',
                         linewidth=6)
    group_yield_bar.legend(loc='upper right', fontsize=40)
    plt.tick_params(labelsize=50)
    plt.title('分档收益均值柱状图', fontsize=50)

    '''IC柱状图'''
    IC_bar = fig.add_subplot(3, 2, 3)
    IC_bar.bar(np.arange(len(ic_series)) + 1, ic_series.values, color='blue')
    IC_bar.plot(np.arange(len(ic_series))+1, [np.nanmean(ic_series.values)] * (len(ic_series)), color='red', label='IC均值', linewidth=6)
    IC_bar.legend(loc='upper right', fontsize=40)
    plt.tick_params(labelsize=50)
    plt.title('因子IC序列柱状图', fontsize=50)

    '''IC衰减'''
    ic_decrease_bar = fig.add_subplot(3, 2, 4)
    ic_decrease_bar.bar(np.arange(ic_decrease_matrix.shape[1])+1, np.array(ic_decrease_matrix.mean(axis=0)), color='green', label='IC衰减')
    plt.tick_params(labelsize=50)
    plt.title('因子IC衰减柱状图', fontsize=50)

    '''多（空）组合收益净值曲线'''
    rev_curve = fig.add_subplot(3, 2, 5)
    rev_curve.plot(np.arange(len(rev_dic['long']['cumu'])) + 1, rev_dic['long']['cumu'], label='多头', linewidth=6)
    rev_curve.plot(np.arange(len(rev_dic['short']['cumu'])) + 1, rev_dic['short']['cumu'], label='空头', linewidth=6)
    rev_curve.plot(np.arange(len(rev_dic['mix']['cumu'])) + 1, rev_dic['mix']['cumu'], label='多空组合', linewidth=6)
    rev_curve.plot(np.arange(len(index_yield_dic['cumu'])) + 1, index_yield_dic['cumu'], label='基准', color='blue', linewidth=6)
    rev_curve.plot(np.arange(len(rev_dic['long']['cumu'])) + 1, np.ones(len(rev_dic['long']['cumu'])), color='black', linewidth=6)
    rev_curve.legend(loc='upper right', fontsize=40)
    plt.tick_params(labelsize=50)
    plt.title('多空（组合）收益序列曲线', fontsize=50)

    '''因子换手率'''
    change_rate_bar = fig.add_subplot(3, 2, 6)
    change_rate_bar.bar(np.arange(len(change_rate_series))+1, change_rate_series.values, color='orange')
    plt.tick_params(labelsize=50)
    plt.title('因子换手率序列柱状图', fontsize=50)

    plt.savefig('backtest_result/' + factor_name + '/' + factor_name + '_' + str(holding_periods) + 'D.png')
    plt.show()
