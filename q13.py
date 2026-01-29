str_a = input("Enter a string: ").lower()

lis = []

for ch in str_a:
    if ch in lis:
        continue
    else:
        lis.append(ch)

lis = "".join(lis)
print("String without duplicates is : ",lis)