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


# print(list_duplicates_of(source, 'B'))
# exit()
# Type word
# wordHangman = input(str("Give word for Hangman:"))
wordHangman = "abbbsfsagcc"
print(wordHangman)

wordHangmanList = list(wordHangman)
secretWord = list(wordHangman)

# Count letters of secret word
result = 0
for char in wordHangman:
    result += 1

# print(result)...

# Alphabetic letters
letters = string.ascii_lowercase
letters = list(letters)
# print(letters)


count_letters = list(range(1, len(secretWord)))


# Replace all letters except the first one with _
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
    # print(list((range(0, len(wordHangmanList)))))
    # print(secretWord)
    str_join = ","
    print(str_join.join(letters))
    letters = list(letters)


    # Add letter(s) to secret word if it correct
    # for letter in wordHangmanList:
    #     if letter == inputLetter:
    #         wordIdx = wordHangmanList.index(letter)
    #         secretWord[wordIdx] = inputLetter

    if inputLetter in wordHangman:
        wordIdx = list_duplicates_of(wordHangman, inputLetter)
        for i in wordIdx:
            secretWord[i] = inputLetter


    word_join = ""
    print(word_join.join(secretWord))
    #print(wordHangman)


    if secretWord == wordHangmanList:
        print("Success")
        break


    # str = ""
    # print(str.join(secretWord))


# print(letters)