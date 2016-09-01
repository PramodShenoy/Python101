#Lists can have any kind of data

l = [1,2,3,4]
print l
l = ['HEY', 'HI', 'HOW ARE YOU?']
print l
l = [2, 'Hello', [4, 56]]
print l




# Lists are mutable
# This implies, that the following will run error-free

l[1] = 100
print l



#Traversing a list using for loop
for element in l:
    print element





# Append and Extend
t1 = ['a', 'b', 'c']
t2 = ['d' 'e']
print t1+t2
t1.extend(t2)
print t1                #Behaves as t1 = t1 + t2
t1.append(t2)
print t1

#sort
t1.sort()






# Deleting elements
t = [1,2,3,4,5,6,7,8,9,10]

#POP - Returns a value; removes from original list
x = t.pop(2)
print x
print t

#REMOVE - removes from original list; element to be deleted is passed as the parameter
t.remove(8)
print t

#DEL - doesnt return the value; deletes from the original list
del t[1:5]
print t




#Function to print all elements in a list

def print_elements(list):
    for element in list:
        t = list()
        if (type(element) == type(t)):
            print_elements(element)
        else:
            print element
