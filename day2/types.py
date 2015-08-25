#!/usr/bin/env python

# Integer
i = 100000

# String
s = "A String"

#Floating point / real number
f = 0.128 

i_as_f = float(i)
f_as_i = int(f)

# Boolean 
truthy = True
falsy = False

# Dictionary 
d1 = { "key1": "value", "key2": "value2"}
d2 = dict(key1="value1", key2="value2")

# Lists -- only one type of item
l = [1,2,3,4,5]
l.append(7)

# Tuple -- multiple types, immutable (cannot add)
t = (1, "blah", 5.1)

# Dictionary- list of tuples
d3 = dict( [ ("key1","value1"), ("key2","value2")])

for value in (i, f, s, truthy, l, t, d1, d2, d3):
    print value, type(value)