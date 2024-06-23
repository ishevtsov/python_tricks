# https://docs.python.org/3.1/library/functions.html#bytearray
# The bytearray type is a mutable sequence of integers in the range 0 <= x <= 255
arr = bytearray((0, 1, 2, 3, 4))
print(arr[1])

print(arr)

arr[1] = 23
print(arr)
print(arr[1])

del arr[1]
print(arr)

arr.append(42)
print(arr)

