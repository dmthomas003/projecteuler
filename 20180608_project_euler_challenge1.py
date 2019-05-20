#!python2

#first project euler challenge
#find the sum of all multiples of three or five bellow 1000

def three(p):
    if p % 3 == 0:
        return True
    else:
        return False

def five(p):
    if p % 5 == 0:
        return True
    else: return False

def sum_three_and_five(p):
    sum_factors = 0
    try:
        for n in range(p):
            if three(n) == True:
                sum_factors += n
            elif five(n) == True:
                sum_factors += n
        return sum_factors
    except TypeError:
        return False

if __name__ == '__main__':
    print sum_three_and_five(1000)
