#!python2
#20180630
#project euler challenge number 7



#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.

#What is the 10,001st prime number?
#this is one version of function that determines if a number is prime or not
def is_primef(number):
    list = [y for y in [number % x for x in range(2,number)] if y == 0]
    if len(list) > 0:
        return False
    else:
        return True




#crude way of eliminating all evens and multiples of previous primes
def n_primef(n):
    list = []
    pre = []
    [pre.append(x) for x in range(2,150000) if x % 2 > 0 or x == 2]
    list += [x for x in pre if [x % y > 0 and x % (y**2) > 0 for y in pre if x != y] and is_primef(x) == True]
    try:
        print len(list)
        print list
        print list[n - 1]
    except IndexError:
        print 'not enough primes'
    

n_primef(10001)
