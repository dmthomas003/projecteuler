#!python2
#20180614
#project euler challenge numbber 4

#Find the largest palindrome made from the product of two 3-digit numbers.


#create a class number that has instance variable value
#method multiply and method plus_one
#recursively multiply two instances of class number
#all int between 99 - 1000 against same
#create method palindrome that determines if a product is a palindrome
def brk():
    print '~~~~~~~~~~~~~~~~~~~~'
class Number(object):
    def __init__(self,value):
        self.value = value
        self.count = value
        self.products = []  #TODO change to universal self.list
    def multiply(self,factor):
        product = self.value * factor
        self.products.append(product)
    def plus_one(self):
        self.value += 1
    def minus_one(self):
        self.value -= 1
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

def is_palindrome(number):
    reverse = str(number)[::-1]
    if str(number) == reverse:
        return True 
    else:
        return False
test00 = Number(999)
test00.auto_minus(100,999)
print test00.products
