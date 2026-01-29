
#---------------------------------
# WITH BUILT-IN FUNCTION
#---------------------------------

s = input("Enter a string : ")
lis = s.split(sep=" ")
for i in range(len(lis) - 1 ,-1,-1):
    print(lis[i] , end= " ")


#---------------------------------
# WITHOUT BUILT-IN FUNCTION
#---------------------------------


s = input("Enter a string : ")
curr_word = ""
words = []

for ch in s:
    if ch != " ":
        curr_word += ch
    else:
        words.append(curr_word)
        curr_word = ""

if curr_word:
    words.append(curr_word)

for i in range(len(words) - 1 , -1 , -1):
    print(words[i],end=" ")