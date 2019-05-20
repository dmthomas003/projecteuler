#!python2
#20180628
#project euler challege number 60

#Find the lowest sum for a set of five primes
#for which any two primes concatenate to produce another prime.
    
def is_primef(number):
    list = [y for y in [number % x for x in range(2,number)] if y == 0]
    if len(list) > 0:
        return False
    else:
        return True #can also return number
list = []
list += [x for x in range(3,100) if is_primef(x) == True] 
prime_pairs = [[(x,y) for y in list if is_primef(int(str(x)+str(y))) == True and is_primef(int(str(y)+str(x))) == True][0][0]
               for x in list if len([(x,y) for y in list if is_primef(int(str(x)+str(y))) == True and is_primef(int(str(y)+str(x))) == True]) >= 5]
'''
def concatenated_pairs(list):
    originals = [x for x in list if x == 3 or x == 7 or x == 109 or x == 673]
    paired = originals + [x for x in list if is_primef(int(str(x)+str(3))) == True and is_primef(int(str(3)+str(x))) == True and is_primef(int(str(x)+str(7))) == True and is_primef(int(str(7)+str(x))) == True and
              is_primef(int(str(x)+str(109))) == True and is_primef(int(str(109)+str(x))) == True and is_primef(int(str(x)+str(673))) == True and is_primef(int(str(673)+str(x))) == True]
    return paired




print concatenated_pairs(list)


##def concatenated_pairs(list):
##    originals = [x for x in list if x == 3 or x == 7]
##    paired = originals + [x for x in list if is_primef(int(str(x)+str(3))) == True and is_primef(int(str(3)+str(x))) == True and is_primef(int(str(x)+str(7))) == True and is_primef(int(str(7)+str(x))) == True]
##    return paired
##print concatenated_pairs(list)
'''

list = []
def prime_list(number,list):
    while number > 1:
        if is_primef(number) == True:
            list.append(number)
            number -= 1
            return prime_list(number,list)
        else:
            number -= 1
            return prime_list(number,list)
    else:
        return list

print prime_list(500,list)
