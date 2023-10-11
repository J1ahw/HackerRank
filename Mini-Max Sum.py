import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    list1 = list(arr)
    results = []
    for i in list1:
        results.append(sum(list1)-i)
    print(min(results), max(results))

arr = (1,2,3,4,5)
miniMaxSum(arr)