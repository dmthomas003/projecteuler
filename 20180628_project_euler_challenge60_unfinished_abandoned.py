#!python2
#20180628
#project euler challege number 60

#Find the lowest sum for a set of five primes
#for which any two primes concatenate to produce another prime.

def is_prime00(number):
    count = 0
    for x in range(2,number)[::-1]:
        if number % x == 0:
            count += 1
            break
        else:
            pass
    if count > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    list = [x for x in range(2,1000) if is_prime00(x) == True]
    concatenated = []
    primes = []
    for x in list:
    #concatenates integer to list conned if integer is the result of two prime numbers concatenated in both orders that itself is a prime
    #adds both ordered concatenations
        primes += [(x,y) for y in list[::-1] if is_prime00(int(str(x)+str(y))) == True and is_prime00(int(str(y)+str(x))) == True]
        ##concatenated += [(int(str(x)+str(y)),int(str(y)+str(x))) for y in list[::-1] if is_prime00(int(str(x)+str(y))) == True and is_prime00(int(str(y)+str(x))) == True]
    print 'Prime numbers in given range'
    print list
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'prime number pairs that when concatenated either way are also prime, i.e 3 and 7: 37, 73'
    print primes
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'should be only matches for each'
    list = [[(x,y) for x in primes if x == y and x[::-1] == y[::-1]] for y in primes]
    print list
    list = []
    for x in primes:
        if x[0] != primes[primes.index(x)-1][0]:
            list.append(x)
        else:
            pass
    #print 'this is list of each prime pair that has at least one concatenation match'
    #print list
    print 'primes with at least one concatenation match'
    print [x[0] for x in primes if x[0] != primes[primes.index(x)-1][0]]    #prints list of primes in range that have concatenation matches
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    master = []
    list = []   
    for x in primes:
        list.append((x[0],len([y[0] for y in primes if x[0] == y[0]])))
        master.append(list[0])
        list = []
    for x in master:
        if x not in list and x[1] >= 5:
            list.append(x)
        else:
            pass
    print 'primes and the total number of matches for each'
    print list
