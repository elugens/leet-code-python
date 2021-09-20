# Problem 3
# -----------------
# Create a function called word_split() which takes in a string phrase and a
# set list_of_words. The function will then determine if it is possible to split
# the string in a way in which words can be made from the list of words. You can
# assume the phrase will only contain words found in the dictionary if it is
# completely splittable.


def word_split(phrase, list_of_words, output=None):
    # Base Case
    if output is None:

        output = []
    # Starting loop phrase to check word matching list of words
    for word in list_of_words:

        # Check for to see if word starts with first word in list_of_words
        if phrase.startswith(word):

            # if the word in phrase matches first word append word to output
            output.append(word)

            # Recursive Call to on next word in list of words
            return word_split(phrase[len(word):], list_of_words, output)

    return(output)


result1 = word_split('themanran', ['clown', 'ran', 'man'])

print(result1)

result2 = word_split('themanran', ['the', 'ran', 'man'])

print(result2)
