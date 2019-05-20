#!python2
#20180708
# project euler challenge 10

def is_primef(n):
    primes = []
    p = n + 1
    bool_list = [True] * p
    for i in range(2,int(p ** 0.5)+1):
        if bool_list[i]:
            for k in range(i ** i, p, i):
                bool_list[k] = False
    for i in range(2,p):
        if bool_list[i]:
            primes.append(i)
    return primes
if __name__ == '__main__':
    print sum(is_primef(2000000))
