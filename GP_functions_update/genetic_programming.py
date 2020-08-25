from create_expression import *
from exchange_expression import *
from variation import *
from fitness import *
from markbaka.element import *
from markbaka.cross_section import *
from markbaka.time_series import *
from markbaka.math import *
from markbaka.constructor_like import *
from markbaka.is_matrix import *
import scipy.io as sio
import time
import os
import random
from datetime import datetime
from load_data import *

def gp(operator, matrix, number, operator_max, operator_min, survive_rate, generations, variation_rate, expression_number, ret):
    """
    Genetic Programming.

    Parameters
    ----------
    operator: list of operators
    matrix: list of matrix
    number: list of number data
    operator_max: max number of operators contained in each expression
    operator_min: min number of operators contained in each expression
    survive_rate: survive_rate in each generation
    generations: circulation generations
    variation_rate: possibility of variation of each expression
    expression_number: the number of expressions created ar first
    ret: stock return matrix

    Returns
    -------
    A collection of expressions

    """
    START = time.time()
    print('Genetic Programming is ready...')
    print('\n\n')

    for generation in range(generations):
        print('Generation: %d' % (generation+1))
        print('\n')
        generation_start = time.time()
        if generation == 0:  # the first circulation
            expression_collection = []
            print('Expressions are building up...\n')
            for i in range(expression_number):
                expression_collection.append(create_expression(operator, matrix, number, operator_max, operator_min))
                print('Expression %d: ' % (i+1), expression_collection[-1])
        print('\nFitness of each expression is under calculation...\n')
        fitness = {}
        for i in range(len(expression_collection)):
            expression_fitness = fitness_icir(eval(expression_collection[i]), ret)
            if expression_fitness in fitness.keys() and not np.isnan(expression_fitness):
                fitness[expression_fitness].append(i)
            elif not np.isnan(expression_fitness):
                fitness[expression_fitness] = [i]
            print('Expression %d: ' % (i+1), expression_fitness)
        fitness_collection = list(fitness.keys())
        fitness_collection.sort(reverse=True)
        survive_number = int(len(expression_collection) * survive_rate)
        new_expression_list = []
        new_expression_index = []
        count = 0
        for i in fitness_collection:
            for j in fitness[i]:
                new_expression_index.append(j+1)
                new_expression_list.append(expression_collection[j])
                count += 1
                if count == survive_number:
                    break
            if count == survive_number:
                break
        print('Remained expressions are: ', new_expression_index)
        expression_collection = new_expression_list

        if generation != generations-1:
            print('\nExpressions are exchanging with each other...\n')
            expression_collection_temp = []
            for i in range(len(expression_collection)):
                index = random.randint(0, len(expression_collection) - 1)
                try:
                    expression_new, temp = exchange_expression(expression_collection[i], expression_collection[index])
                except:
                    expression_new = expression_collection[i]
                expression_collection_temp.append(expression_new)
                print('New expression %d: ' % (i + 1), expression_collection_temp[-1])
            expression_collection = expression_collection_temp

            print('\nExpressions are mutating...\n')
            for i in range(len(expression_collection)):
                judge = random.random()
                if judge > variation_rate:
                    print('According to the possibility, expression %d does not mutate successfully' % (i + 1))
                    continue
                else:
                    try:
                        expression_collection[i] = variation(expression_collection[i], operator, matrix, number,
                                                         operator_max // 2, operator_min=operator_min // 2)
                        print('Expression %d mutates successfully' % (i + 1))
                        print('Expression %d: ' % (i+1), expression_collection[i])
                    except:
                        print('Expression %d does not mutate successfully' % (i+1))

        generation_end = time.time()
        print('\nGeneration %d is finished...' % (generation+1))
        print('Time: %.2fs\n\n' % (generation_end-generation_start))

    print('Genetic Programming is over...')
    END = time.time()
    print('Total Time: %.2fs' % (END-START))

    if 'Factor_Expressions.csv' not in os.listdir('factor_result'):
        record = pd.DataFrame(columns=['GP_Index', 'Expression_Index', 'Expressions'])
    else:
        record = pd.read_csv('factor_result/Factor_Expressions.csv', index_col='Date', parse_dates=['Date'])
    if record.shape[0] == 0:
        gp_index = 1
    else:
        gp_index = record.iloc[-1, 0] + 1
    print('Finally, we get these expressions:')
    for i in range(len(expression_collection)):
        print(expression_collection[i])
        information = [gp_index, i+1, expression_collection[i]]
        data_add = pd.Series(information, index=['GP_Index', 'Expression_Index', 'Expressions'])
        data_add.name = datetime.now()
        record = record.append(data_add)
        record.to_csv('factor_result/Factor_Expressions.csv', index=True)
        record.index.name = 'Date'
        data = eval(expression_collection[i])
        sio.savemat('factor_result/factor_'+str(information[0])+'_'+str(information[1])+'.mat',
                    {'factor_'+str(information[0])+'_'+str(information[1]): data})











