def rev_word(s):
    """
    Manually doing the splits on the spaces.
    """
    breakpoint()

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    breakpoint()

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words))


sentWord = ' Hello World '

print(rev_word(sentWord))
