    
# ranges/lists/tuples and strings
a = "This is a string"
b = [1,4,9,25,36]
c = (1,4,9,25,36)
d = range(5,15)
e = list(range(10))
f = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
 
# ranges are "lists" of sequential numbers not stored in memory
g = [5,6,7,8,9,10,11,12,13,14]
g = list(range(5,10))

h = [0,1,2,3,4]
h = list(range(5))


print(a[0])
print(b[1])
print(c[-1])   # index from the back
print(d[:3])   # elements 0,1,2
print(e[1:3])  # elements 1,2 
print(f[1])    
print(f[1][1])
print(f[1][2:]) # elements 3,4
    
     
# a[1] = 1     
# c[1] = 1     
# d[1] = 1

b[0] = 0
b[1:4] = [1,2,3,4]
b[-1] = 10
f[0] = 10
f[1] = [0,0,0,0]
f[1][2] = 5 
 
# function definitions
   
def myadd(a, b):
    return (a+b)

print(myadd(10,20)) 
     
myadd = lambda a, b : a+b

print(myadd(10,20))


# list comprehension
a = [i for i in range(5)]    
b = [i*i for i in range(5) if i % 2 == 0]    
c = [myadd(10,i) for i in range(5)]   
d = [i+j for i in range(2) for j in range(2)]  
     
print(a)
print(b)
print(c)
print(d)

# a generator
squares = (i*i for i in range(21))

# i*i is computed here
for s in squares:
   print(s)
   
# an iterator empties out as you read elements from it
# nothing is printed here
for s in squares:
   print(s)
   
# a function which creates generators
def createSquares(n):
    mylist = range(n)
    for i in mylist:
        yield i*i

# the generator is created here
squares = createSquares(21)

# i*i is computed and printed here
for s in squares:
   print(s)
   

# a list
# i*i is computed here
squares = [i*i for i in range(21)]
for s in squares:
   print(s)
   
 
# map, filter and reduce
import functools
a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
b = list(map( lambda x: x*x, a))
print(b)  

b = list(filter(lambda x: x < 10,b))
print(b)

mysum = functools.reduce(lambda x, y: x+y, b)
print(mysum)

# without lambdas
def myadd(x,y):
  return x+y
mysum = functools.reduce(myadd, b)
print(mysum)

# these two have the same result
d = list(zip([1,2,3],[4,5,6])) 
print(d)
     
d = [(1,4),(2,5),(3,6)] 
print(d)

# Possible implementations of the functional operations     
mymap = lambda f, ls : [f(x) for x in ls]

print(mymap(lambda x : x*x, [1,2,3,4]))

def mymap(f, ls):
    return [f(x) for x in ls]

print(mymap(lambda x : x*x, [1,2,3,4]))

myfilter = lambda p, ls : [x for x in ls if p(x)]

print(myfilter(lambda x : x < 5, [1,2,3,4,5,6,7,8,9,10]))

def myfilter(p, ls):
    return [x for x in ls if p(x)]

print(myfilter(lambda x : x < 5, [1,2,3,4,5,6,7,8,9,10]))






            


    



#
# solution 1 - familiar approach
#
# create container for squares
squares = []
for i in range(21):
    # append adds an element to the back of a list
    squares.append(i*i)      
     
# create container for odd squares
oddsquares = []
for i in range(21):
    if i % 2  == 1: oddsquares.append(i*i)

# create a function for alternating sum
def altsum(ls):
    sgn = 1
    retval = 0
    for i in ls:
        retval += i * sgn
        sgn = -sgn
    return retval

# print results
print("sum:", altsum(squares))
print("sum:", altsum(oddsquares))

#
# solution 2 - using list comprehension 
#
# create containers
squares = [i*i for i in range(21)]
oddsquares = [i*i for i in range(21) if i % 2 == 1]

# define function to be used twice
def altsum(ls):
    # zip takes a pair of lists and creates a list of tuples
    # sum takes a container and returns the sum of the entries
    return sum([(-1)**j*i for (i, j) in zip(ls, range(21))])

print("sum:", altsum(squares))
print("sum:", altsum(oddsquares))


#
# solution 3 - using map
#
# create containers
squares = map(lambda x : x*x , range(21))
oddsquares = map(lambda x : (2*x+1)**2, range(10))

altsum = lambda ls : sum([(-1)**j*i for (i, j) in zip(ls, range(21))])

print("sum:", altsum(squares))
print("sum:", altsum(oddsquares))



