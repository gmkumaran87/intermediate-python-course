#!/bin/python3
import timeit
import time
import datetime

# Complete the factorial function below.
# Factorial function using Recusive can produce result upto 998 and results in error maximum Recursive function
# if n = 999
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

'''if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)'''

# Factorial using bottom up approach using list can produce results if n = 100000
def fact(n):
    if n ==0 or n == 1:
        return 1
    fact_lst =[]
    fact_lst.append(0)
    fact_lst.append(1)
    fact_lst.append(2)

    for i in range(3, n+1):
        fact_lst.append(i)
        fact_lst[i] = fact_lst[i] * fact_lst[i-1]
    return fact_lst[n]

#a = datetime.datetime.now()
code_to_test = ''''
print(fact(100000))'''
#b = datetime.datetime.now()

elapsed_time = timeit.timeit(code_to_test,number=100)/100
print(elapsed_time)
#print(factorial(999))


