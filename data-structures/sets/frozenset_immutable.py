# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('p')

d = {frozenset({1,2,3}): 'hello'}
print(d)

print(d[frozenset({1,2,3})])