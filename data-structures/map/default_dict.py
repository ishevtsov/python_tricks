# collections.defaultdict
# https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict
dd = defaultdict(list)

#  Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])