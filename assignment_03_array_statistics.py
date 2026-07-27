# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



num_list = []

def main():
    number = int (input("how many numbers? "))
    i = 1

    if number <=0 :
        print("enter a number greater than 0")
        return 

    while i <= number:
        input_score = int(input(f"Enter number {i}: "))
        num_list.append(input_score)
        i += 1

    print("\nResults:")
    sum_function()
    average()
    maximum()
    minimum()

def sum_function():
    total_sum = 0 
    for num in num_list:
        total_sum += num
    print(f"sum: {total_sum}")


def average():
    total_average = 0
    for num in num_list:
        total_average += num

    total_average /= len(num_list)
    print(f"Average: {total_average}")    

def maximum():
    max_value = num_list[0]
    for i in range(1, len(num_list)):
        if max_value < num_list[i]:
            max_value = num_list[i]
    print(f"maximum: {max_value}")

def minimum():
    minimum_value = num_list[0]
    for i in range(1, len(num_list)):
        if minimum_value > num_list[i]:
            minimum_value = num_list[i] 
    print(f"maximum: {minimum_value}")



main()