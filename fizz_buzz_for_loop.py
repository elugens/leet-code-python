for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
        continue

    if i % 3 == 0:
        print('Fizz')
        continue

    if i % 5 == 0:
        print('Buzz')
        continue

    else:
        print(i)
