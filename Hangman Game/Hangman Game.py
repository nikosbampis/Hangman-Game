import string

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


wordHangman = "abbbsfsagcc"
print(wordHangman)

wordHangmanList = list(wordHangman)
secretWord = list(wordHangman)

# Count letters of secret word
result = 0
for char in wordHangman:
    result += 1

# Alphabetic letters
letters = string.ascii_lowercase
letters = list(letters)

# Replace all letters except the first one with _
count_letters = list(range(1, len(secretWord)))
for char in count_letters:
    secretWord[char] = "_"

for i in range(8):
    inputLetter = input(str("Give Letter: "))

    # Ask for only ONE letter (need correction)???
    if len(inputLetter) >= 2:
        print("Type only ONE letter")
        inputLetter = input(str("Give Letter: "))
    else:
        print("The letter you type is", inputLetter)

    # Remove typing letter from alphabetic list
    for lowerc in letters:
        if lowerc == inputLetter:
            letters.remove(lowerc)

    str_join = ","
    print(str_join.join(letters))
    letters = list(letters)

    if inputLetter in wordHangman:
        wordIdx = list_duplicates_of(wordHangman, inputLetter)
        for i in wordIdx:
            secretWord[i] = inputLetter

    word_join = ""
    print(word_join.join(secretWord))

    if secretWord == wordHangmanList:
        print("Success")
        break