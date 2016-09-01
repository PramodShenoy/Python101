# Declaring tuples

tup = ()
print type(tup)

tup = 'a', 
print type(tup)

tup = 'a', 'b'
print type(tup)

a = 1
b = 2
tup = a, b
print type(tup)


# Split into charecters
tup = tuple('Hello!')
print tup

# Indexing like an array
element = tup[2]
print element

# Slicing
print tup[1:5]

#Modifying a tuple isnt allowed, but one tuple can be replaced with another
tup = ('A',) + tup[:]
print tup




#easy assignment ; eg. Exchanging two values

x = 5
y = 10

temp = x
x = y
y = temp

print x, y

x = 5
y = 10

x, y = y, x

print x, y




# eg. Split method that works exactly like lists'

email = 'gakharsushant@gmail.com'
uname, domain = email.split('@')
print uname, domain




# Tuples as return values

def ret_tuple(x, y):
    q = x/y
    r = y/x
    return q, r

q1, r1 = ret_tuple(10, 5)

print q1, r1
    




#Variable number of elements

def print_arguments(*args):
    print args

print_arguments(1, 4, 5, 6)


# Scattering of elements
t = (10, 5)
q, r = ret_tuple(*t)
print q, r
# q, r = ret_tuple(t) # will give an error





#Zip function - creates a list

def zip_func(t1, t2):
    for a, b in zip(t1, t2):
        if a == b:
            print a, b


t1 = (1, 2, 3, 4, 5)
t2 = (1, 7, 2, 4, 0)
zip_func(t1, t2)



#Enumerate function - gives index and value of he element

l = [1, 2, 3, 4]
for index, element in enumerate(l):
    print index, element



# Functions with dictionaries

d = {'a':0, 'b':1, 'c':2, 'd':3}
tup = d.items()
print tup

t1 = ('a', 'b', 'c')
t2 = (1, 2, 3)
l = zip(t1, t2)
print l
di = dict(l)
print di


d2 = dict(zip('abc', range(3)))
print 'd2', d2


