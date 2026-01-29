#---------------------------------
# STRING PALINDROME
#---------------------------------

str_a = input("Enter string : ")
n = len(str_a)
if n % 2 == 0 :
    n1 = int(n / 2)
    s1 = str_a[:n1]
    s2 = str_a[n:n1-1:-1]
    if s1 == s2:
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    left = 0
    right = n
    mid = int((( left + right ) / 2 ) + 0.5 )
    right -= 1
    while ( left < mid ) and ( right > mid ):
        if str_a[left] == str_a[right]:
            left += 1
            right -= 1
        else:
            print("Not a Palindrome")
            break
    if right == mid:
        print("Palindrome")
        

#---------------------------------
# NUMBER PALINDROME
#---------------------------------

num = int(input("Enter a number: "))
n = num
rev_num = 0
while(n > 0):
    last = n % 10
    n = n // 10
    rev_num = rev_num * 10 + last

if num == rev_num :
    print("Palindrome")
else :
    print("Not a Palindrome")
