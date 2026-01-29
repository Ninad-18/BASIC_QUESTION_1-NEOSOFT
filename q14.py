n = int(input("Enter a number : "))
div = []

for i in range(1,n):
    if n % i == 0 :
        div.append(i)
        
print(div)
if sum(div) == n :
    print("Its a perfect number")
else:
    print("Its not a perfect number")