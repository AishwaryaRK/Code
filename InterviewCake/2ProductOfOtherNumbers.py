def get_products_of_all_ints_except_at_index(numbers):
    product_numbers = []
    before_product = 1
    prev_number = 1
    for n in numbers:
        product_numbers.append(before_product * prev_number);
        before_product = before_product * prev_number
        prev_number = n
    print(product_numbers)

    after_product = 1
    prev_number = 1
    for i, n in reversed(list(enumerate(numbers))):
        product_numbers[i] *= after_product * prev_number
        after_product = after_product * prev_number
        prev_number = n
    print(product_numbers)

get_products_of_all_ints_except_at_index([3, 1, 2, 5, 6, 4])
