#
# 6 - Sum Square Difference
#
'''
    The sum of the squares of the first ten natural numbers is,
        1² + 2² +...+ 10² = 385
        
    The square of the sum of the first ten natural numbers is,
        (1 + 2 +...+ 10)² = 55² = 3025
        
    Hence the difference between the sum of the squares of the first 
    ten natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first 
    one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(sum_range):
    sum_square = 0
    for number in range(1, sum_range+1):
        sum_square += number ** 2
    return sum_square


def square_of_sums(sum_range):
    square_sum = 0
    for number in range(1, sum_range+1):
        square_sum += number
    square_sum **= 2
    return square_sum


def difference(n1, n2):
    return n2 - n1


def main():
    index_range = 10
    # index_range = 100

    res1 = sum_of_squares(index_range)
    res2 = square_of_sums(index_range)
    result = difference(res1, res2)

    print(f"\nThe difference between the sum of the squares and the square of")
    print(f"the sums in the range between {res2} and {res1} is: {result}")


# start application
if __name__ == "__main__":
    main()
