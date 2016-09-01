fout = open('demofile.txt', 'w')
print fout
print fout.name

line1 = 'Text to be written\n'
fout.write(line1)
line2 = 'Second line of text to be written\n'
fout.write(line2)
line3 = 'Third line of text to be written\n'
fout.write(line3)

fout.close()
 


#Format operator

fout = open('demofile1.txt', 'w')
x = 23
fout.write(str(x) + '\n')
fout.write('I spotted %d %s' % (10, 'camels'))
x = 23
print str(23)




# In the above statements, the all the format operater must
# correspond with the contents of the tuple
 


fout.close()





#Reading files
fin = open('demofile.txt')           # Will work with 'r'
for line in fin:
    print line





#SEEK METHOD

fin = open('demofile2.txt', 'r')

fin.seek(2)
line = fin.read()
print line

fin.seek(1, 2)
line = fin.read()
print line

fin.seek(2, 2)
line = fin.read()
print line
