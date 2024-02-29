#
# 3 - Largest Prime Factor
#
'''
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 6000851475143?
'''


def find_prime_factors(passed_value):
    prime_factors = []
    for number in range(1, passed_value+1):
        if passed_value % number == 0:
            prime_factors.append(number)
    return prime_factors


def main():
    passed_value = 13195
    # passed_value = 600851475143       # takes too much time in python
    result = find_prime_factors(passed_value)

    print(f"Prime Factors List: ")
    print(result)
    print(f"Largest Prime Factor (other than itself): {result[len(result)-2]}")


# start application
if __name__ == "__main__":
    main()
