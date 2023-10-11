import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s.split(':')[0]
    minute = s.split(':')[1]
    second = re.sub("[^0-9]", "", s.split(':')[2])
    if 'AM' in s:
        if hour == '12':
            hour = '00'
    else:
        if hour != '12':
            hour = str(int(hour) + 12)
    return(f'{hour}:{minute}:{second}')

S = '07:05:45PM'
print(timeConversion(S))