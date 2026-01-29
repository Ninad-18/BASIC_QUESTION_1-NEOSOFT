n = int(input("Enter number: "))
if n <= 0:
    print("No Fibonacci numbers to display.")
elif n == 1:
    print("Fibonacci Sequence is: 0")
else:
    first = 0
    second = 1
    print("Fibonacci Sequence is:", first, second, end=" ")
    for _ in range(n - 2):
        c = first + second
        print(c, end=" ")
        first = second
        second = c
    print()