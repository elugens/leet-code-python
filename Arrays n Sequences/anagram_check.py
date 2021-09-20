def anagram(a, b):

    a = a.replace(' ', '').lower()
    b = b.replace(' ', '').lower()

    return sorted(a) == sorted(b)


print(anagram('godd', 'dog'))
