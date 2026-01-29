vow_1 = "aeiou"
vow_2 = "AEIOU"
count = 0
str_a = input("Enter string : ")
for i in range(len(str_a)):
    if str_a[i] in vow_1 or str_a[i] in vow_2:
        count += 1

print("No. of vowels is : ",count)