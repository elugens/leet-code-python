# Py Practice
def printodd():

    start, end = 1, 10

    for num in range(start, end + 1):

        if num % 3 == 0 or num == 1:
            print(num, end=" ")

    print("End Results")


printodd()
