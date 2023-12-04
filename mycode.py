# Read contents of Dictionary.txt into an array of strings

with open('Dictionary.txt', 'r') as f:
    word_list = f.read().splitlines()

# Check if each string in the array is a palindrome

palindrome_list = []
for word in word_list:
    if word == word[::-1]:
        palindrome_list.append(word)


print(palindrome_list)