# collections.OrderedDict
# https://docs.python.org/3/library/collections.html#collections.OrderedDict

import collections

d = collections.OrderedDict(one=1, two=2, three=3)
print(d)

d['four'] = 4
print(d)

print(d.keys())