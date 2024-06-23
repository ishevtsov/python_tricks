# collections.ChainMap
# https://docs.python.org/3/library/collections.html#collections.ChainMap

from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

print(chain)

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
print(chain['three'])
print(chain['one'])
print(chain['missing'])
