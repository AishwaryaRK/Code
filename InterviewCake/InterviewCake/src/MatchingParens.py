def get_closing_paren(sentence, opening_paren_index):
    opening_parens_count = 0
    given_paren_count_number = -1
    for index, c in enumerate(sentence):
        if c == '(':
            opening_parens_count += 1
            if index == opening_paren_index:
                given_paren_count_number = opening_parens_count
        if c == ')':
            if opening_parens_count == given_paren_count_number:
                return index
            opening_parens_count -= 1


print get_closing_paren(
    "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)

# 57-78
# 68-77