#!python2
#project euler challenge number (2)
#By considering the terms in the Fibonacci sequence whose values do not
#exceed four million, find the sum of the even-valued terms.

def fibonocci(number,list):
    fib_sum = 0
    while number <= 4000000:
        if number == 1:
            list.append(number)
            return fibonocci(number + 1,list)
        elif number == 2:
            list.append(number)
            return fibonocci(number + (number - 1),list)
        else:
            list.append(number)
            return fibonocci(number + list[list.index(number)-1],list)
    else:
        for fib in list:
            if fib % 2 == 0:
                fib_sum += fib
        return fib_sum,list
fib_list = []
print fibonocci(1,fib_list)
