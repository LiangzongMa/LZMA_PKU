# 遗传规划
# 使用说明：
# '''A'''：设置随机交换两棵二叉树的移动步数范围
# '''B'''：设置子树自发变异的随机移动步数范围
# '''C'''：自由设计Fitness计算适应度的函数
# '''D'''：自由定义符号集中每个符号对应的运算
# '''E'''：自由设置初始随机生成的树的数量
# '''F''': 设置变异概率
# Length 用来控制大概的公式长度
# 若最后还希望计算根据表达式得到的因子值，做微小修改就可以
# 以下输出的表达式都使用后缀表达式（也即树的后根周游）
import warnings
import random
import fitness  # 适应度计算模块
import calculate
import time
import numpy as np
import DataSet
import pandas as pd
from datetime import datetime
warnings.filterwarnings("ignore")


# 需要用到的数据结构：二叉树，队列，栈
# 队列的有关操作，第一个元素是Q[header]
class Queue(object):
    def __init__(self, header=0, rear=0, Content=None):
        self.header = header
        self.rear = rear
        self.Content = Content

    # 创建一个空队列
    def CreateNullQ(self):
        Q = Queue()
        Q.Content = []
        return Q

    # 队尾进入一个元素
    def InsertQ(self, x):
        self.rear += 1
        self.Content.append(x)

    # 队首出一个元素并返回出列元素
    def PopQ(self):
        x = self.Content[self.header]
        self.header = self.header + 1
        return x

    # 判断队列是不是空
    def JudgeNull(self):
        if self.header == self.rear:
            return 1
        else:
            return 0


# 二叉树有关操作
class RandomBiTree(object):
    # 初始化一棵二叉树
    def __init__(self, left=None, right=None, parent=None, info=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.info = info

    # 随机生成一棵二叉树，调用数据集Data与符号集Character
    def CreateTree(self, Data, Character, Length):
        lenData = len(Data)  # 获取数据集的大小
        lenCharacter = len(Character)  # 获取符号集的大小
        # 创建一个初始队列
        Q = Queue().CreateNullQ()
        # 随机生成第一个符号元素，进入队列
        FC = Character[random.randint(0, lenCharacter - 1)]
        Q.InsertQ([FC, self])
        # 每次从队列中出一个元素，如果出来的元素是数，那么就不再进入队列，否则进入两个元素，进入的元素和出去的元素形成父和子节点的关系
        # 判断进入为数据还是运算符
        # 在0与1之间随机生成一个，如果为0，则进入数据，为1则进入运算符，Length用来控制生成的表达式的长度
        # 随机生成两个元素
        while not Q.JudgeNull():
            [Parameter, Adress] = Q.PopQ()
            Adress.info = Parameter
            if Parameter not in Data:
                Adress.left = RandomBiTree()
                Adress.left.parent = Adress
                Adress.right = RandomBiTree()
                Adress.right.parent = Adress
                DataSelect1 = random.randint(0, 1)
                if DataSelect1 == 1 and Q.rear <= (Length // 2):
                    SecondSelect1 = random.randint(0, lenCharacter - 1)
                    Q.InsertQ([Character[SecondSelect1], Adress.left])
                else:
                    SecondSelect1 = random.randint(0, lenData - 1)
                    Q.InsertQ([Data[SecondSelect1], Adress.left])
                DataSelect2 = random.randint(0, 1)
                if DataSelect2 == 1 and Q.rear <= (Length // 2):
                    SecondSelect2 = random.randint(0, lenCharacter - 1)
                    Q.InsertQ([Character[SecondSelect2], Adress.right])
                else:
                    SecondSelect2 = random.randint(0, lenData - 1)
                    Q.InsertQ([Data[SecondSelect2], Adress.right])
        return self

    # 随机交换两棵二叉树的部分子树，交换思路是：生成一个移动步数x，让指针从根部随机走动，当走到叶节点则不随机向下走，但是可以向回走，x次操作后，交换
    def ChangeTree(self, Tree):
        '''A'''
        Steps = random.randint(30, 50)
        Tree1 = self
        Tree2 = Tree
        for i in range(Steps):
            Direction = random.randint(0, 2)
            if Direction == 0 and Tree1.left is not None:
                Tree1 = Tree1.left
            elif Direction == 1 and Tree1.right is not None:
                Tree1 = Tree1.right
            elif Tree1.parent is not None:
                Tree1 = Tree1.parent
        for i in range(Steps):
            Direction = random.randint(0, 2)
            if Direction == 0 and Tree2.left is not None:
                Tree2 = Tree2.left
            elif Direction == 1 and Tree2.right is not None:
                Tree2 = Tree2.right
            elif Tree2.parent is not None:
                Tree2 = Tree2.parent
        Mid = Tree2
        if Tree2.parent is not None and Tree2.parent.left == Tree2:
            P = Tree2.parent
            Tree1.parent = P
            Tree2.parent.left = Tree1
        elif Tree2.parent is not None and Tree2.parent.right == Tree2:
            P = Tree2.parent
            Tree1.parent = P
            Tree2.parent.right = Tree1
        elif Tree2.parent is None:
            Tree = Tree1
            Tree.parent = None
        if Tree1.parent is not None and Tree1.parent.left == Tree1:
            P = Tree1.parent
            Mid.parent = P
            Tree1.parent.left = Mid
        elif Tree1.parent is not None and Tree1.parent.right == Tree1:
            P = Tree1.parent
            Mid.parent = P
            Tree1.parent.right = Mid
        elif Tree1.parent is None:
            Mid.parent = None
            self = Mid
        return [self, Tree]

    # 子树变异，这里不考虑点变异
    def Mutate(self, Data, Character, Length):
        Tree = RandomBiTree()
        Tree.CreateTree(Data, Character, Length)
        '''B'''
        Steps = random.randint(30, 50)
        Tree1 = self
        for i in range(Steps):
            Direction = random.randint(0, 2)
            if Direction == 0 and Tree1.left is not None:
                Tree1 = Tree1.left
            elif Direction == 1 and Tree1.right is not None:
                Tree1 = Tree1.right
            elif Tree1.parent is not None:
                Tree1 = Tree1.parent
        if Tree1.parent is not None and Tree1.parent.left == Tree1:
            P = Tree1.parent
            Tree.parent = P
            Tree1.parent.left = Tree
        elif Tree1.parent is not None and Tree1.parent.right == Tree1:
            P = Tree1.parent
            Tree.parent = P
            Tree1.parent.right = Tree
        elif Tree1.parent is None:
            Tree.parent = None
            self = Tree
        return self

    # 后根周游二叉树
    def lastOrder(self, list):
        if self.left is not None:
            self.left.lastOrder(list)
        if self.right is not None:
            self.right.lastOrder(list)
        if self is not None:
            list.append(self.info)


# 运用二叉树的内容来设计遗传规划算法
# 设计适应度函数，见引入模块
'''C'''


# 遗传规划具体算法，传入三个参数，数据集Data，符号集Character，遗传代数Generation
def GP(FileName, Data, Character):
    GoodTreeCollection = []
    TREENUMBER, Length, Generation, DieRate = DataSet.BasicGPDataSet()
    print("正在导入计算适应度所需的数据")
    t1 = time.time()
    OpenPrice = np.load('OpenPrice5M_1Day.npy')
    t2 = time.time()
    print("导入成功，用时：%.2f" % (t2-t1), '秒')
    TIME_START = time.time()
    # 定义运算符号，在引入模块
    '''D'''

    # 计算每棵树的因子值
    def CalculateTree(Tree):
        Array = []
        Tree.lastOrder(Array)  # 得到了二叉树的后根周游结果
        Stack = []
        for k in range(len(Array)):
            if Array[k] in Data:
                Stack.append(Array[k])
            if Array[k] in Character:
                Data2 = Stack.pop()
                Data1 = Stack.pop()
                DataCalculated = calculate.Calc(Data1, Data2, Array[k], FileName)
                Stack.append(DataCalculated)
        return Stack[0]

    # 随机生成一些棵树
    '''E'''
    print("准备生成原始的父代二叉树\n")
    TreeNumber = random.randint(TREENUMBER[0], TREENUMBER[1])
    Tree = []  # 储存生成的树
    for i in range(TreeNumber):
        mid = []
        print("准备尝试生成一棵树")
        tree = RandomBiTree()
        tree.CreateTree(Data, Character, Length)
        tree.lastOrder(mid)
        print("生成第%d棵树成功" % (i+1))
        print(mid, '\n')
        Tree.append(tree)
    TreeNumber = len(Tree)

    print("\n\n准备对生成的树进行淘汰")
    print("本次淘汰的比率为：", DieRate, '\n')
    for i in range(Generation-1):
        print("准备开始进行第%d次淘汰" % (i+1))
        Fitness = []
        for j in range(TreeNumber):
            time_start = time.time()
            Factor = CalculateTree(Tree[j])
            while type(Factor) != np.ndarray:
                print("第%d棵树由于不包含有效数据，重新建树" % (j+1))
                mid = []
                print("准备尝试生成一棵树")
                tree = RandomBiTree()
                tree.CreateTree(Data, Character, Length)
                tree.lastOrder(mid)
                print("生成第%d棵树成功" % (j + 1))
                Tree[j] = tree
                print(mid)
                Factor = CalculateTree(Tree[j])
            mid = []
            Tree[j].lastOrder(mid)
            '''下面部分是为了剔除量价相关性这样的广为人知的因子'''
            CorrVP = 0
            for k in range(len(mid)-2):
                Price = ['ClosePrice5M_5Day', 'OpenPrice5M_5Day', 'HighPrice5M_5Day', 'LowPrice5M_5Day']
                Volume = ['RealVolume5M_5Day', 'StockAmount5M_5Day']
                if mid[k] in Price:
                    if mid[k+1] in Volume:
                        if mid[k+2] == 'Corr':
                            CorrVP = 1
                if mid[k] in Volume:
                    if mid[k+1] in Price:
                        if mid[k+2] == 'Corr':
                            CorrVP = 1
            F = fitness.CalcFitness(Factor, OpenPrice)
            if CorrVP == 1:
                F = F * 0.75
            ''''''
            if F > 0.6:
                mid = []
                Tree[j].lastOrder(mid)
                GoodTreeCollection.append(mid)
            time_end = time.time()
            print("第%d棵树的适应度为：" % (j+1), F)
            Fitness.append(F)
            print("第%d课树适应度计算完毕" % (j+1))
            print("用时：%.2f" % (time_end-time_start), '秒\n')
        Fitness = np.array(Fitness)
        Index = np.argsort(-Fitness)
        TreeNumber = int(TreeNumber * DieRate) // 2 * 2
        print("筛选后得到的树的索引为：", np.array(Index[0:TreeNumber])+1)
        NewTree = []
        for j in range(TreeNumber):
            NewTree.append(Tree[Index[j]])
        Tree = NewTree
        # 现在Tree中储存的是按照适应度从大到小排列的经过第一次筛选后的树，进行两两之间的交叉互换
        print("\n\n淘汰完毕，准备两两交叉互换")
        j = 0
        while j < TreeNumber:
            ChangeTree = Tree[j].ChangeTree(Tree[j + 1])
            Tree[j] = ChangeTree[0]
            Tree[j + 1] = ChangeTree[1]
            mid0 = []
            Tree[j].lastOrder(mid0)
            mid1 = []
            Tree[j+1].lastOrder(mid1)
            print("经过交叉互换后的第%d棵树为" % (j + 1), mid0, '\n')
            print("经过交叉互换后的第%d棵树为" % (j + 2), mid1, '\n')
            j += 2

        # 对交叉后的树再进行变异
        '''F'''
        Percent = 0.5
        print("\n\n准备对交叉后的树进行随机变异")
        print("随机变异的概率为：", Percent)
        for j in range(TreeNumber):
            Mid = Tree[j]
            Judge = random.random()
            if Judge <= Percent:
                print('变异成功')
                Mid = Mid.Mutate(Data, Character, Length)
            else:
                print("根据概率，此次不进行变异")
            Tree[j] = Mid
            mid = []
            Tree[j].lastOrder(mid)
            print("变异后的第%d棵树为" % (j + 1), mid, '\n')
        print("第%d次淘汰，交叉，变异过程结束\n" % (i+1))

    i = Generation - 1
    print("准备开始进行第%d次淘汰" % (i + 1))
    Fitness = []
    for j in range(TreeNumber):
        time_start = time.time()
        Factor = CalculateTree(Tree[j])
        while type(Factor) != np.ndarray:
            print("第%d棵树由于不包含股票数据，重新建树" % (j + 1))
            mid = []
            print("准备尝试生成一棵树")
            tree = RandomBiTree()
            tree.CreateTree(Data, Character, Length)
            tree.lastOrder(mid)
            print("生成第%d棵树成功" % (j + 1))
            Tree[j] = tree
            print(mid)
            Factor = CalculateTree(Tree[j])
        F = fitness.CalcFitness(Factor, OpenPrice)
        if F > 0.6:
            mid = []
            Tree[j].lastOrder(mid)
            GoodTreeCollection.append(mid)
        time_end = time.time()
        print("第%d棵树的适应度为：" % (j + 1), F)
        Fitness.append(F)
        print("第%d课树适应度计算完毕" % (j + 1))
        print("用时：%.2f" % (time_end - time_start), '秒\n')
    Fitness = np.array(Fitness)
    Index = np.argsort(-Fitness)
    TreeNumber = int(TreeNumber * DieRate) // 2 * 2
    print("筛选后得到的树的索引为：", np.array(Index[0:TreeNumber]) + 1)
    NewTree = []
    for j in range(TreeNumber):
        NewTree.append(Tree[Index[j]])
    print("第%d次淘汰，交叉，变异过程结束" % (i + 1))

    '''表达式输出和存储'''
    expression_collection = pd.read_csv('Factor_Collection.csv').set_index('Date')
    times = expression_collection.iloc[expression_collection.shape[0] - 1, 0]
    print("最终筛选出的树的表达式为：")
    for j in range(TreeNumber):
        mid = []
        NewTree[j].lastOrder(mid)
        new_factor = pd.DataFrame(
            np.array([datetime.now(), times + 1, mid]).reshape(1, 3),
            columns=['Date', 'Total_Time', 'Expression'])
        new_factor = new_factor.set_index('Date')
        expression_collection = expression_collection.append(new_factor, ignore_index=False)
        print("第%d棵" % (j+1), mid)
    TIME_END = time.time()
    print("\n以下是所有过程挑选出的可能有效的树：")
    for j in range(len(GoodTreeCollection)):
        new_factor = pd.DataFrame(
            np.array([datetime.now(), times + 1, GoodTreeCollection[j]]).reshape(1, 3),
            columns=['Date', 'Total_Time', 'Expression']).set_index('Date')
        expression_collection = expression_collection.append(new_factor, ignore_index=False)
        print("第%d棵：" % (j+1), GoodTreeCollection[j])
    expression_collection.to_csv('Factor_Collection.csv')
    print("\n本次遗传规划一共耗时：%.2f" % (TIME_END - TIME_START), '秒')
    print("程序运行完毕")




