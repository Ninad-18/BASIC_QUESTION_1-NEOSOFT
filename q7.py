s1 = input("Enter string 1: ").replace(" ","").lower()
s2 = input("Enter string 2: ").replace(" ","").lower()

if len(s1) != len(s2):
    print("Strings are not anagrams")
else:
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        print("The Strings are anagrams")
    else:
        print("Strings are not anagrams")

