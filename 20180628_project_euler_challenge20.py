#!python2
#20180628
#project euler challenge number 20

#sum of digits of integer 100!

def factorial(number):
    count = 1
    for integer in range(1,number + 1):
        count *= integer
    return count
factorial_onehundred = factorial(100)
sum_of_factorial = 0
for x in str(factorial_onehundred):
    sum_of_factorial += int(x)
print sum_of_factorial
