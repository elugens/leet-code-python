# The difference between the Append and Extend methods
arr = ['cat', 'dog', 'rabbit']

arr2 = ['horse', 'turtle']

arr.append(arr2)

print(arr)

print('\n')

arr3 = ['cat', 'dog', 'rabbit']

arr4 = ['horse', 'turtle']

arr3.extend(arr4)

print(arr3)
