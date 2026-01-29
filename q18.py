def check_prime_factor(n,f):

    if f<= 1 or n % f != 0:
        return "Not a Prime Factor"
    
    for i in range(2,f):
        if f % i == 0:
            return ("Not a Prime Factor")
        
    return ("It's a Prime Factor")

n = int(input("Enter main number : "))
f = int(input("Enter a factor to check : "))
print(check_prime_factor(n,f))