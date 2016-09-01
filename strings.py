s = 'examplestring'
print s

#indexing of strings
letter = s[1]
print letter 

last_letter = s[-1]
print last_letter

last_letter = s[-2]
print last_letter 


#length function
l = len(s)
print l 
print '\n'



#traversal of string
prefixes = 'JKLMNOPQ'
suffix = 'ACK'

for p in prefixes:
    print p + suffix



#string slicing
s1 = s[:7]
s2 = s[1:7]
s3 = s[8:]
print s1, s2, s3




# Question - Check what s[:] gives


# string functions
S = s.upper()
print S
s = S.lower()
print s

fruit = 'bananas'
print fruit.find('a')
print fruit.find('a',2)
print fruit.find('s',2,6)


# String comparisions
if fruit < 'Pineapple':
    print fruit, 'is lesser than Pineapple'
if fruit > 'Pineapple':
    print fruit, 'is greater than Pineapple'
if fruit == 'Pineapple':
    print fruit, 'is Pineapple'




# Example 

word = 'abcdef abc abc'
count = 0
letr = 'a'
for let in word:
    if(let == letr):
        count = count + 1
print count
