def palindrome(number):
    return int(str(number)[::-1]) == number

largest_palindrome = 0

for num1 in range(999, 99, -1):
    for num2 in range(num1, 99, -1):
        product = num1 * num2
        if palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)

assert (palindrome(906609)), "Got a wrong answer"

assert(largest_palindrome == 906609), "Got a wrong answer"