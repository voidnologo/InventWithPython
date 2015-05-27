keep_going = True

print("Type 'quit' as one of your words to quit.")
while keep_going:
    print("Enter a word: ")
    word1 = input()

    print("Enter another word: ")
    word2 = input()

    if word1 == 'quit' or word2 == 'quit':
        keep_going = False

    if word1 < word2:
        print (word1 + " comes before " + word2)
    if word1 > word2:
        print (word2 + " comes before " + word1)
    if word1 == word2:
        print (word1 + " is the same as " + word2)
