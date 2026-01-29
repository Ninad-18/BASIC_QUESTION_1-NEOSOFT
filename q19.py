def gcd(n1, n2):
    gcd_val = 1
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd_val = i
    return gcd_val

def lcm(n1,n2):
    lowest = (n1 * n2)//gcd(n1,n2)
    print(f"LCM of {n1} and {n2} is : {lowest}")


n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
lcm(n1,n2)