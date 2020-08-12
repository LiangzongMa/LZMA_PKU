from single_factor_analyzer import *
import os

if __name__ == '__main__':
    parent_file = os.path.dirname(__file__)
    file_collection = os.listdir(os.path.join(parent_file, 'factor_database'))
    for i in file_collection:
        try:
            backtest = single_factor_analyzer(
                i[:-4],
                high_limit=1,
                low_limit=0,
                holding_periods=2,
                percent=0.003,
            )
            backtest.back_test_run()
        except:
            continue
        else:
            print(i+'处理完毕\n')
