while True:
    line = raw_input('>>')
    if line == 'done':
	break
    print line

print 'DONE!'


a = raw_input('Enter the value of a\n')
a = int(a)
while not (a < 1):
    print a
    a-=1


    
