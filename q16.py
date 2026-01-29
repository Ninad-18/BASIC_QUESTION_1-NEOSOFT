n = int(input("Enter a number: "))

if n == 0:
    print("Decimal to Binary conversion of 0 is 0")
else:
    binr = ""
    n1 = n
    while n > 0:
        dig = n % 2
        binr += str(dig)
        n //= 2
    print(f"Decimal to Binary conversion of {n1} is", binr[::-1])
