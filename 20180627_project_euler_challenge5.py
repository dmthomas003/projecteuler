#!python2
#20180627
#project euler challenge number 5
#What is the smallest positive number
#that is evenly divisible by all of the numbers from 1 to 20?
def brk():
    print '~~~~~~~~~~~~~~~~~~~~'
def prnt(n):
    print n
class Number(object):
    def __init__(self,value):
        self.value = value
        self.count = value
        self.list = []
        self.products = []
        self.divisors = []
    def multiply(self,factor):
        self.list = []
        product = self.value * factor
        self.list.append(product)
        self.products.append(product)
    def plus_one(self):
        self.value += 1
    def minus_one(self):
        self.value -= 1
    def auto_multiply(self,limit):    #non inclusive so limit is set by rule
        while self.count < limit:    # not decided at function level/ +1 from desired
            self.count += 1     #starts multiplication at 1 not 0
            self.multiply(self.count)
    #list of products of range integer +1 from specified
    #start as indicated in function call as argument
    def multiply_iterative(self,integer,low):  #low and integer are inclusive
        self.list = [n * self.value for n in range(low,integer + 1)]
    def multiply_iterative_double(self,integer,low):  #low and integer are inclusive
        self.list = [n * x for n in range(1,self.value + 1) for x in range(low,integer + 1)]
    #multiplies then reduces self recursively until zero, resets and repeats
    #until count == set limit
    def recursive_multiply(self,limit,original):
        while self.value > 0:
            self.multiply(self.count)
            self.value -= 1
        else:
            while self.count < limit:
                self.count += 1
                self.value = original
                self.recursive_multiply(limit,original)
        self.value = original
    def auto_plus(self,limit,original):
        while self.value < limit:
            self.multiply(self.count)
            self.plus_one()
        else:
            while self.count < limit:   
                self.count += 1 
                self.value = original
                self.auto_plus(limit,original)
    def auto_minus(self,limit,original):    #set the recursion limit and 
        while self.value > limit:#store original value
            self.multiply(self.count)
            self.minus_one()    #run multiply and subtract one from value
        else:   #until value == limit then incriment count and do again
            while self.count > limit:#until count == limit
                self.count -= 1
                self.value = original
                self.auto_minus(limit,original)
    #returns true if the number reads the same written forwards and backwards
    def is_palindrome(self):
        reverse = str(self.value)[::-1]
        if str(self.value) == reverse:
            return True
        else:
            return False
    #returns true if given divisor returns zero modulo with self.value
    def modulo(self,divisor):
        if self.value % divisor == 0:
            return True
        else:
            return False
    def modulo_iterative(self,divisors):
        self.divisors = [n for n in divisors if self.modulo(n) == True]

target01 = Number(20)
print target01.value
target01.multiply_iterative(12000000,11000000)
print target01.list
targets01 = [Number(n) for n in target01.list]
[n.modulo_iterative(range(1,target01.value +1)) for n in targets01]
divisors = [n for n in targets01 if len(n.divisors) == target01.value]
brk()
print [n.value for n in divisors]
brk()
