#Give values for x and y

x = 10 
y = 10
print 'x =', x
print 'y =', y

#Checking all conditions
#Checking equality after operation

if(x%2 == 0):
    print x, 'is even'

if(y%2 == 1):
    print y, 'is odd'

#Not equal
if(x!=y):
    print 'x and y are not equal'

#Greater than
if(x>y):
    print 'x is greater than y'

#Greater than equal to
if(x>=y):
    print 'x is greater than, or equal to y'

#Lesser than
if(x<y):
    print 'x is lesser than y'

#Lesser than equal to
if(x<=y):
    print 'x is lesser than, or equal to y'




#if-elif-else

if(x>y):
    print 'x is greater'
elif(y>x):
    print 'y is greater'
else:
    print 'x is equal to y'
