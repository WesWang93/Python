#=========================================================================================
#Name: FizzBuzz
#Author: Wesley Wang
#Date: 4/12/2018
#=========================================================================================

"""
This function return interger 1 ~ 100
If the number is divisible by 3, return "Fizz"
If the number is divisible by 5, return "Buzz"
If the number is divisible by 3 and 5, reutnr "FizzBuzz"
"""
def fizz_buzz():
    result = ""
    for i in range(1, 101):
        #Return
        if i%3 != 0 and i%5 !=0:
            result += str(i)
        if i%3 == 0:
            result += "Fizz"
        if i%5 == 0:
            result += "Buzz"
        result += '\n'
    return result

print(fizz_buzz()) #Print fizz_buzz