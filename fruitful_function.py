import math

def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    d = (dy**2) + (dx**2)
    d1 = math.sqrt(d)

    return d1


#Explain int() function
x1 = int(raw_input('Enter x1\n'))
y1 = int(raw_input('Enter y1\n'))
x2 = int(raw_input('Enter x2\n'))
y2 = int(raw_input('Enter y2\n'))



dist = distance(x1, y1, x2, y2)
print dist
