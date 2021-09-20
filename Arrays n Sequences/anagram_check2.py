def anagram2(a, z):

    a = a.replace(' ', '').lower()
    z = z.replace(' ', '').lower()

    if(len(a) != len(z)):
        return False

    count = {}

    breakpoint()  # This is how you set a break point

    for letter in a:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in z:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    for k in count:
        if count[k] != 0:

            return False

    return True


if __name__ == "__main__":
    print(anagram2('god', 'god'))
