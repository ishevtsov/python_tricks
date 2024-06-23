# types.MappingProxyType
# https://docs.python.org/3/library/types.html#types.MappingProxyType

from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])
# read_only['one'] = 23

writable['one'] = 42
print(read_only)