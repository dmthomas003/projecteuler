#!python2
#20180628
#project euler challenge number 6

#Find the difference
#between the sum of the squares of the first one hundred natural numbers
#and the square of the sum.

sum_squared = 0
sum_squares = 0
squares = [x**2 for x in range(1,101)]
for x in range(1,101):
    sum_squared += x
sum_squared = sum_squared ** 2
for x in squares:
    sum_squares += x
print sum_squares
print sum_squared
print sum_squared - sum_squares
