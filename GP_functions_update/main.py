from load_data import *
from genetic_programming_settings import *
from genetic_programming import *


if __name__ == '__main__':
    gp(operator=operator,
       matrix=matrix,
       number=number,
       operator_max=operator_max,
       operator_min=operator_min,
       survive_rate=survive_rate,
       generations=generations,
       variation_rate=variation_rate,
       expression_number=expression_number,
       ret=ret)
