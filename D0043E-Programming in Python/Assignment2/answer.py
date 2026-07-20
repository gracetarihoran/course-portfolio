'''
Author: Grace Tarihoran

Generate random number between 0-999
Print random numbers as many as the user wants
Display numbers unsorted
Separate even and odd numbers
Display numbers sorted (asc for even and desc for odd)
'''

import random

# --- Constants ---
MIN_RANDOM = 0
MAX_RANDOM = 999
INVALID_INPUT_MESSAGE = "Invalid Input"


def bubble_sort(items):
    ''' Return new list sorted in ascending '''

    result = items[:]
    n = len(result)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
    return result


def list_to_string(_list):
    ''' Return the list as one string separated by space '''

    list_string = ""
    i = 0

    while i < len(_list):
        list_string = list_string + str(_list[i])

        if i < len(_list) - 1:
            list_string = list_string + " "
        i += 1
    return list_string


def main():
    ''' Read input, generate random numbers, call functions, and print the result '''

    # read and validate count
    try:
        random_num = int(input("How many random numbers in the range 0 - 999 are desired? "))
        if random_num <= 1:
            print(INVALID_INPUT_MESSAGE)
            return
    except ValueError:
        print(INVALID_INPUT_MESSAGE)
        return

    try:
        # generate random numbers and save in numbers list
        numbers = []
        i = 0

        while i < random_num:
            numbers.append(random.randint(MIN_RANDOM, MAX_RANDOM))
            i += 1

        # print unsorted numbers
        print(f"\nHere are the random numbers:\n{list_to_string(numbers)}")
    except MemoryError:
        print("Impossible to handle the requested amount of numbers on this system.")
        return

    try:
        # split numbers list into even and odd list
        even_numbers = []
        odd_numbers = []

        for num in range(len(numbers)):
            num_value = numbers[num]

            if num_value % 2 == 0:
                even_numbers.append(num_value)
            else:
                odd_numbers.append(num_value)

        # sorting even and odd list
        sorted_even_num = bubble_sort(even_numbers)
        sorted_odd_num = bubble_sort(odd_numbers)
        sorted_odd_num.reverse()

        # print and check if even or odd list are empty
        if len(sorted_even_num) == 0:
            sorted_even_num_str = "No Even Numbers"
        else:
            sorted_even_num_str = list_to_string(sorted_even_num)   # convert list values to a string separated by space

        if len(sorted_odd_num) == 0:
            sorted_odd_num_str = "No Odd Numbers"
        else:
            sorted_odd_num_str = list_to_string(sorted_odd_num)   # convert list values to a string separated by space

        print(f"\nHere are the random numbers arranged:\n{sorted_even_num_str} - {sorted_odd_num_str}")
        print(f"\nOf the above {random_num} numbers, {len(even_numbers)} were even and {len(odd_numbers)} odd")
    except ValueError:
        print(INVALID_INPUT_MESSAGE)
    except MemoryError:
        print("Impossible to handle the requested amount of numbers on this system.")


# Run the program
if __name__ == "__main__":
    main()
