# inititalizong dictionaries

eng2sp = dict()
print eng2sp

eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

print eng2sp

print eng2sp['two']
#print eng2sp['four']

sp2eng = {'uno':'one', 'dos':'two', 'tres':'three'}
print type(sp2eng)


#Length function

print len(eng2sp)




# in operator compares with keys, NOT values; This is because keys are unique
print 'one' in eng2sp
print 'uno' in eng2sp




# dict.values() returns a list of all values. dict.keys() returns a list of all keys
values = eng2sp.values()
print values
keys = eng2sp.keys()
print keys



# Example question - histogram function that records the number of occurence of each letter in a string

def hist(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
    	    d[c] = 1

    return d



#Example question - inverting a dictionary

def invert_dict(d):
    inverse = dict()
    for key in d: 
        val = d[key]
        if val in inverse:
	    inverse[val].append(key)
        else:
            inverse[val] = [key]

    return inverse



