#
# 4 - Largest Palindrome Product
#
'''
    A palindromic number reads the same both ways. The largest palindrome 
    made from the product of two 2-digit numbers is 9009 = 91 * 99.
    
    Find the largest palindrome made from the product of two 3-digit 
    numbers.
'''

def find_palindromes():
    palindrome_list = []
    for number1 in range(100, 999):
        for number2 in range(100, 999):
            result = number1 * number2
            is_palindrome = isolate_digits(result)
            if is_palindrome:
                palindrome_list.append(result)
    return palindrome_list


def isolate_digits(result):
    result_to_string = str(result)
    digits = []
    for digit in result_to_string:
        digits.append(int(digit))
    return compare_digits(digits)


def compare_digits(digits):
    validator1 = False
    validator2 = False
    validator3 = False
    try:
        if digits[0] == digits[5]:
            validator1 = True
        if digits[1] == digits[4]:
            validator2 = True
        if digits[2] == digits[3]:
            validator3 = True
    except(IndexError):
        pass
    if validator1 and validator2 and validator3:
        return True
    return False


def find_highest(palindromes):
    highest_number = 0
    for number in palindromes:
        if number > highest_number:
            highest_number = number
    return highest_number


def main():
    palindromes = find_palindromes()
    highest_palindrome = find_highest(palindromes)

    print("The Palindrome Product list is as follows: ")
    print(palindromes)
    print(f"\nThe highest Palindrome made from the product of two 3-digit number is: {highest_palindrome}")


# start application
if __name__ == "__main__":
    main()
