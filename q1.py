str_a = input("Enter a string to reverse: ")

# With Indexing
rev = ""
for i in range(len(str_a) - 1,-1,-1):
    rev += str_a[i]

print("Reversed String with indexing : ",rev)


# Without Indexing 

print("Reversed String without indexing : ",str_a[::-1])