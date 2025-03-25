import numpy as np
import time
def sort_comparison(n):
    result1 = np.empty(1000)
    for i in range(1000):
        a = np.random.rand(n)
        time1 = time.time()
        b = np.sort(a, kind='quicksort')
        time1 = time.time()- time1
        result1[i] = time1
    result2 = np.empty(1000)
    for i in range(1000):
        a = np.random.rand(n)
        time1 = time.time()
        b = np.sort(a, kind='mergesort')
        time1 = time.time()-time1
        result2[i] = time1
    result3 = np.empty(1000)
    for i in range(1000):
        a = np.random.rand(n)
        time1 = time.time()
        b = np.sort(a, kind='heapsort')
        time1 = time.time() - time1
        result3[i] = time1
    print ("quicksort average {}, max {}".format(np.average(result1), np.max(result1)))
    print ("mergesort average {}, max {}".format(np.average(result2), np. max(result2)))
    print ("heapsort average {}, max {}".format(np.average(result3), np.max(result3)))