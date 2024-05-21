def fizz_buzz(n: int):
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        print(i)

fizz_buzz(20)