for i in range(1, 1001):
    print("Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or str(i))
