str_a = input("Enter a string/sentence: ").lower()

letters = set()

for ch in str_a:
    if 'a'<=ch<='z':
        letters.add(ch)

if len(letters) == 26:
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")