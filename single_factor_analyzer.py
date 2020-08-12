from preprocess_operations import *
from ic_operations import *
from yield_operations import *
from picture_operations import *
from factor_changerate_operations import *
import time

class single_factor_analyzer:
    def __init__(self,
                 factor_name,
                 index_name='000905.SH',
                 start_date='2017-01-03',
                 end_date='2020-07-01',
                 holding_periods=5,
                 group_number=10,
                 percent=0.1,
                 high_limit=0.975,
                 low_limit=0.025):
        self.factor_name = factor_name
        self.index_name = index_name
        self.start_date = start_date
        self.end_date = end_date
        self.holding_periods = holding_periods
        self.group_number = group_number
        self.percent = percent
        self.high_limit = high_limit
        self.low_limit = low_limit

    def back_test_run(self):
        print('回测程序开始运行\n')
        start_time = time.time()
        '''建立回测结果文件夹'''
        create_result_file(self.factor_name)

        '''因子导入与预处理'''
        # 导入数据并根据持仓日期计算收益率
        print('正在导入数据...')
        data_dic = load_data(self.factor_name, self.index_name, self.start_date, self.end_date)
        factor = data_dic[self.factor_name]
        index = data_dic[self.index_name]
        open = data_dic['open']
        yield_matrix = open.pct_change(periods=1)
        print('数据导入完毕！\n')

        # 去极值，横截面标准化，市值中性，行业中性
        print('正在进行因子的进一步处理...')
        factor = winsorize_cross(factor, self.low_limit, self.high_limit)
        print('去极值完毕！')
        factor = standardize_cross(factor)
        print('横截面标准化完毕！')
        factor = size_neutralize(factor)
        print('市值中性完毕！')
        factor = industry_neutralize(factor)
        print('行业中性完毕！')
        print('因子进一步处理完毕！\n')

        # 计算ic，ic衰减
        print('正在计算IC与IC衰减...')
        ic = ic_calculate(factor, yield_matrix, periods=1)
        print('IC计算完毕！')
        ic_decrease_matrix = ic_decrease(factor, yield_matrix, periods=10)
        print('IC衰减计算完毕！\n')

        # 计算收益率
        print('正在进行收益率的有关计算...')
        index_Yield = index_yield(index)
        print('目标指数收益序列计算完毕！')
        yield_collection = Yield(ic, self.factor_name, self.holding_periods, self.percent, factor, yield_matrix=yield_matrix)
        print('多/空/多空组合收益序列计算完毕！')
        group_yield_collection = group_yield(self.holding_periods, factor, yield_matrix, self.group_number)
        print('分档多头净值序列计算完毕！\n')

        # 计算因子换手率
        print('正在计算因子换手率...')
        change_rate_series = factor_change_rate(yield_collection['weight'])
        print('换手率计算完毕！\n')

        # 做图
        print('正在做图...')
        picture(self.factor_name, group_yield_collection, ic, self.holding_periods, ic_decrease_matrix, yield_collection, index_Yield, change_rate_series=change_rate_series)
        print('做图完毕！\n')

        end_time = time.time()
        print('回测运行结束，用时：%.2f秒' % (end_time-start_time))
