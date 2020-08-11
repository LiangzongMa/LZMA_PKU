# 遗传规划主函数
import os
from gp import *
import DataSet
Path = 'DataBase'
os.chdir(Path)


if __name__ == '__main__':
    print("程序启动\n\n")
    FileName, TotalData, Charactor = DataSet.BasicDataSet()
    print("\n准备开始进行遗传规划")
    while 1:
        GP(FileName, TotalData, Charactor)
