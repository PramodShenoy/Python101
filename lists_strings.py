s1 = 'spam'
t1 = list(s1)
print t1

s2 = 'ab cd ef gh'
t2 = s2.split()
print t2

s3 = 'spam-spam-spam'
delimiter = '-'
t3 = s3.split(delimiter)
print t3


s4 = delimiter.join(t2)
print s4
