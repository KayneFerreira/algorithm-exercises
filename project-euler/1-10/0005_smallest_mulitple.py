#
# 5 - Smallest Multiple
#
'''
    2520 is the smallest number that ca be divided by each of the numbers
    from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?
'''

def smallest_divisible_number(start, end):
    index = 1
    while True:
        for number in range(start, end+1):
            print(f"Range: {number} - Number: {index}")
            if index % number != 0:
                break
            if number == end:
                return index
        index += 1


def main():
    start = 1
    end = 10    # anything above 16 takes too much time in python
    result = smallest_divisible_number(start, end)

    print(f"\nThe smallest positive number that is evenly divisible by all ")
    print(f"of the numbers from 1 to {end} is: {result}")


# start application
if __name__ == "__main__":
    main()
