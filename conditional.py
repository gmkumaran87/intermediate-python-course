import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 0 and N in list(range(2, 6)):
        print('Not Weird')
    elif N % 2 == 0 and N in list(range(6, 21)):
        print('Weird')
    elif N % 2 == 0 and N > 20:
        print('Not Weird')
    elif N % 2 == 1:
        print('Weird')