def words_count(s):
    count = 0 
    in_word = False

    for ch in s:
        if ch != " " and not in_word:
            count += 1
            in_word = True
        elif ch == " ":
            in_word = False
        
    return count 

s = input("Enter a string : ")
count = words_count(s)
print("No. of words in the sentence is:", count)