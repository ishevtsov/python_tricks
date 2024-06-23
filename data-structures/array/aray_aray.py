# https://docs.python.org/3/library/array.html
import array
arr = array.array('f', (1.0, 2.0, 1.5, 2.5))
print(arr[1])

print(arr)

arr[1] = 23.0
print(arr)

del arr[1]
print(arr)

arr.append(42.0)
print(arr)

# Arrays are typed
#arr[1] = 'hello'