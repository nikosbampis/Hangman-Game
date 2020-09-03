import string

#wordHangman = input(str("Give word for Hangman:"))
wordHangman = "test"
print(wordHangman)

wordHangman = list(wordHangman)


result = 0
for char in wordHangman:
    result += 1

#print(result)...

letters = string.ascii_lowercase
letters = list(letters)
print(letters)

count_letters = list(range(1, len(wordHangman)))
print(count_letters)


for char in count_letters:
    wordHangman[char] = "_"

print(wordHangman)
