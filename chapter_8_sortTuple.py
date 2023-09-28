d = {'a':10, 'b':1, 'c': 22}
# t = sorted(d.items())
# print(t)
# for k, v in sorted(d.items()) :
#   print(k, v)


# This code is the same output above.
# List Comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
print(sorted( [(v, k) for k, v in d.items() ] ) )
