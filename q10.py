num = int(input("Enter number : "))
n = len(str(num))
num1 = num
new_num = 0
while (num1 > 0):
    digit = num1 % 10
    new_num += pow(digit,n)
    num1 = num1 // 10

if new_num == num:
    print("Its a Armstrong number")
else:
    print("Its not a Armstrong number")
