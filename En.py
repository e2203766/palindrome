with open('words.txt', 'r') as f:
    word_list = f.read().splitlines()

# Check if each string in the array is a palindrome
count = 0
for word in word_list:
    if str(word) == str(word)[::-1]:
        count += 1

print("Number of palindromes in words.txt:", count)
