# -*- coding: utf-8 -*-

import time
import multiprocessing as mp

st1 = 3
st2 = 5


core_count = mp.cpu_count() * 2
total_itr = 1000000000          # Use maximum number your computer can compute within 1min

list1 = []
list2 = []

def serial_pi():
    reduced_sum1 = 0.0
    reduced_sum2 = 0.0

    st_time = time.time()
    list1 = range(st1, total_itr, 4)
    list2 = range(st2, total_itr, 4)

    for i, j in zip(list1, list2):
        reduced_sum1 += (1.0 / float(i))
        reduced_sum2 += (1.0 / float(j))

    result = 4.0 * ( 1.0 + (reduced_sum2 - reduced_sum1))

    print("\n[Serial Pi] After %s iterations PI: %s # Time taken : %s secs\n" % (total_itr, result, round(time.time() - st_time, 5)))

def parallel_pi():

    # ToDo: Initalize the list1, list2 in parallel
    # ToDo: Calculate the reduced sums of the inverse of the element in lists in parallel
    # Todo: calculate result

    # Hint: You can use openmp implementation for python for distribute the task using all the cores

    pass

if __name__ == '__main__':
    serial_pi()

    # ToDo: Implement the parallel section

    # Can you estimate the relation between memory consumption and the total iteration???
