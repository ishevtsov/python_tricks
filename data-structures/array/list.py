# https://docs.python.org/3.6/library/stdtypes.html#lists
arr = ['one', 'two', 'three']
print(arr[0])
print(arr)

arr[1] = 'hello'
print(arr)

del arr[1]
print(arr)

arr.append(23)
print(arr)