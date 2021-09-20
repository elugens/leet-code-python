import collections


def finder3(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


arr1 = [4, 4, 7, 9]
arr2 = [4, 4, 7]

print(finder3(arr1, arr2))
