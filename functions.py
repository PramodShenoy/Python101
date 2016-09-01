import math

p = math.pi

s = math.sin(p)
c = math.cos(p)
t = math.tan(p)


def print_ratios(s1,c1,t1):
    print 'sin is', s
    print 'cos is', c
    print 'tan is', t

def print_global_ratios():
    global s, c, t
    print s, c, t


#Might print slightly incorrect values. 
print_global_ratios()
print_ratios(s,c,t)





