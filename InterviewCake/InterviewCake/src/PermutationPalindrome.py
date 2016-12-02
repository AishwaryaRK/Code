def has_permutation_palindrome(str):
    unpaired_chars = set()
    for c in str:
        if c in unpaired_chars:
            unpaired_chars.remove(c)
        else:
            unpaired_chars.add(c)
    return len(unpaired_chars) <= 1

print has_permutation_palindrome("dccssss")
