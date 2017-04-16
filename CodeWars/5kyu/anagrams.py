def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]


    """anagrams = []
    sorted_words = []
    sorted_word = "".join(sorted(word))
    for i in words:
        s_words = sorted(i)
        o_words = "".join(s_words)
        sorted_words.append(o_words)
    for w in sorted_words:
        if sorted_word in sorted_words:
            anagrams.append(w)
    return anagrams """





print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))