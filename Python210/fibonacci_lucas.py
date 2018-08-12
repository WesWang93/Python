#=========================================================================================
#Name: Fibonacci Series & Lucas Number
#Author: Wesley Wang
#Date: 4/12/2018
#=========================================================================================

"""
Calculate value at nth position by using the formula f(n)=f(n-2)+f(n-1)
:param: First num in series, Second num in series, Nth position to return
:return: Value at Nth position
"""
def sum_series(n0, n1, nth):
    prev = n0
    current = n1
    if nth > 2:
        for i in range(nth-2):
            prev, current = current, prev + current
    if nth == 1:
        return prev
    elif nth <= 0:
        return "Please enter a non-zero, positive number!"
    else:
        return current

#Pass in 0 and 1 as first two values and nth to sum_series to calculate value at nth position
def fibonacci(nth):
    return sum_series(0, 1, nth)

#Pass in 2 and 1 as first two values and nth to sum_series to calculate value at nth position
def lucas(nth):
    return sum_series(2, 1, nth)


assert fibonacci(5) == 3 #Check if 5th number of Fibonacci series is 3, throws exception if not
assert lucas(5) == 7 #Check if 5th number of Lucas series is 3, throws exception if not

