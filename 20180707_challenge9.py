#!python2
#20180707


#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a_b = [x for x in range(1,200000) if (x ** 0.5) - int((x** 0.5)) == 0.0]
print a_b
list = [[(x,y,(x + y)) for x in a_b] for y in a_b[::-1]]
c = []
for x in list:
    for y in x:
        for z in a_b:
            if z == y[2]:
                c.append((y,z))
print c

a_b_c = []
for x in c:
    if int(x[0][1]**0.5)+int(x[0][2]**0.5)+int(x[0][0]**0.5) == 1000:
        a_b_c.append((int(x[0][1]**0.5),int(x[0][2]**0.5),int(x[0][0]**0.5),int(x[0][1]**0.5)+int(x[0][2]**0.5)+int(x[0][0]**0.5)))
print a_b_c
