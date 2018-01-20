# This is a comment
print("Hello World")

# Variable declarations
a = 10
b = 10.0
c, d = 3,2  # simultaneosly assigns c and d 
e = "Hello World"
f = True

# Type information
print(a, " is of type ", type(a)) 
print(b, " is of type ", type(b)) 
print(c, " is of type ", type(c)) 
print(d, " is of type ", type(d)) 
print(e, " is of type ", type(e)) 
print(f, " is of type ", type(f))
    
print(2**3)    # exponentiation 
print(10 / 4)  # float division
print(10 / 2)  # float division 
print(10// 4)  # integer division

print(True and False)
print(True or False)
print(not False)

if 11 > 10: print("True")
else: print("False")

if 11 > 10: print("True");  print("Twice") 
else: print("False");  print("Twice")

if 11 > 10:
    print("True") 
else:
    print("False")    
    
if 10 > 11: 
    print("False")
    print("Twice")
elif 11 > 10:
    print("True")
    print("Twice")
else:
    print("False")
    print("Twice")
    
    
i = 0
while i < 10:
    print(i)
    i += 1

for i in range(100):
    print(i)

for i in range(10):
    for j in range(10):
        print((i,j))
    

def myadd(a, b):
    return a+b

print(myadd(10,20))
print(myadd(10.1,20.1))

myadd = lambda a, b: a+b

print(myadd(10,20))
print(myadd(10.1,20.1))


 #import everything, but change name
import random as rnd
 # call function by
print(rnd.random())
