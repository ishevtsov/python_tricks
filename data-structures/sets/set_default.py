#v https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
vowels = {'a','e','i','o','u'}
print('e' in vowels)

letters = set('alice')

print(letters.intersection(vowels))

vowels.add('x')
print(vowels)
print(len(vowels))