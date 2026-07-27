# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



# PART A - Print the First N Terms
def generate_fibonacci():
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    if n == 1:
        print("Fibonacci sequence: 0")
        return

    fib = [0, 1]
    for i in range(2, n):
        next_term = fib[-1] + fib[-2]
        fib.append(next_term)

    # Print the terms on one line separated by spaces
    print("Fibonacci sequence:", *fib)


# PART B - Check if a Number Belongs to the Sequence
def check_fibonacci():
    try:
        num = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if num < 0:
        print(f"{num} is NOT a Fibonacci number.")
        return

    # Generate Fibonacci numbers until we reach or exceed the target number
    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


# ======================================================================
# Execution
# ======================================================================
if __name__ == "__main__":
    print("--- PART A ---")
    generate_fibonacci()
    
    print("\n--- PART B ---")
    check_fibonacci()