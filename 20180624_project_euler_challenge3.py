#!python2
#20180624 Project Euler Challenge number 3
#What is the largest prime factor of the number 600851475143 ?
#super ugly, but we got there.  Need to refine before posting online
#prime is 6857

def brk():
    print '~~~~~~~~~~~~~~~~~~~~~~~~'    
def is_prime(number):
    factor_list = []
    try:
        for x in range(number):
            if x <= 1 or x == number:
                pass
            elif number % x == 0:
                    factor_list.append(x)
            else:
                pass
    except MemoryError:
        smaller = 1000000
        for x in range(smaller):
            if x <= 1 or x == number:
                pass
            elif number % x == 0:
                    factor_list.append(x)
            else:
                pass
    if len(factor_list) > 0:
        return False,factor_list
    else:
        return True


    
def factors(p,n,list):   #p is original number, n is recursive
    if n == p:
        list = []
        return factors(p,(n-1),list)
    elif n == 1:
        return list
    else:
        if p % n == 0:
            list.append(n)
            return factors(p,(n-1),list)
        else:
            return factors(p,(n-1),list)

def factors01(p,n):
    if is_prime(p) == True:
        return p
    elif is_prime(n) == True:
        if p % n == 0:
            return n
    else:
        return factors01(p,(n-1))
factor_list = []
print is_prime(11),'prime'
print is_prime(9),'not prime'
brk()
print 'is_prime(7)'
print is_prime(7)
print 'is_prime 600851475143'
print is_prime(600851475143)
print is_prime(13195)
print is_prime(486847)
'''
brk()
print 'factors01(26,26)'
print factors01(26,26)
print 'faactors01(600851475143,600851475143)'
print factors01(600851475143,600851475143)
'''
