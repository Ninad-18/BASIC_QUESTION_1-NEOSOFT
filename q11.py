yr = int(input("Enter a year: "))

if (yr % 400 == 0):
    print("Leap Year")
elif ( yr % 100 != 0 ) and (yr % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")