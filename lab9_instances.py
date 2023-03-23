'''
lab9
instance
'''

from lab9_class import my_stat

my_cal_instance = my_stat()

print(my_cal_instance.cal_sigma(3,5))

print(my_cal_instance.cal_pi(3,5))

print(my_cal_instance.cal_fact(5))

print(my_cal_instance.cal_perm(5,2))

import numpy as np

print(np.math.factorial(999))
print(my_cal_instance.cal_fact(999))
