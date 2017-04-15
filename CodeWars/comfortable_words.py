def comfortable_word(word):
    left = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    Right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
    index_of_character = ""
    for w in word:
        word.index[w] % 2 == 0 and w in left:
            return True
        else:
            return False

comfortable_word("test")
comfortable_word("yams")
print(comfortable_word("yams"))
print(comfortable_word("test"))