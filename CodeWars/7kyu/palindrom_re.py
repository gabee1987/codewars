from collections import Counter

def palindrome_rearranging(s):
    return sum(v % 2 == 1 for v in Counter(s).values()) <= 1



print(palindrome_rearranging("abbcabb"))
print(palindrome_rearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))
print(palindrome_rearranging("zyyzzzzz"))



def can_permutation_palindrome(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    odd_count = 0
    for count in counter.values():
        odd_count += count % 2
    return odd_count in [0, 1]
    print(odd_count)

can_permutation_palindrome("abbcabb")
can_permutation_palindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc")
can_permutation_palindrome("zyyzzzzz")