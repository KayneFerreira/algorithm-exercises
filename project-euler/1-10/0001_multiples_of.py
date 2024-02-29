#
# 1 - Multiples of 3 or 5
#
'''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
'''

def find_multiples_of(value):
    multiples = []
    for number in range(value):
        if number % 3 == 0:
            multiples.append(number)
        if number % 5 == 0:
            multiples.append(number)
    return multiples


def sum_multiples(multiples):
    sum = 0
    for number in multiples:
        sum += number
    return sum


def main():
    passing_value = 10
    # passing_value = 1000
    multiples = find_multiples_of(passing_value)
    result = sum_multiples(multiples)

    print(f"The sum of all multiples of 3 and 5 below {passing_value} is: {result}")


# start application
if __name__ == "__main__":
    main()