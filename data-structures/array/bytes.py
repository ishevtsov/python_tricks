# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# (integers in the range of 0 <= x <= 255)
arr = bytes((0, 1, 2, 3))
print(arr[1])

print(arr)

arr = b'\x00\x01\x02\x03'
print(arr)

# arr = bytes((0, 300))

# arr[1] = 23

# del arr[1]