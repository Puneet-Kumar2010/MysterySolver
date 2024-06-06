import re
import math
import time

def sort_numbers(input_string):
    input_string = re.sub(r'\D', ' ', input_string)
    input_list = list(map(int, input_string.split()))
    input_list.sort()
    return input_list

def get_first_number(input_list):
    return input_list[0]

def get_last_number(input_list):
    return input_list[-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    return [num for num in numbers if is_prime(num)]

def find_composites(numbers):
    return [num for num in numbers if not is_prime(num)]

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def find_even_numbers(numbers):
    return [num for num in numbers if is_even(num)]

def find_odd_numbers(numbers):
    return [num for num in numbers if is_odd(num)]

def is_divisible_by(n, divisor):
    return n % divisor == 0

def find_divisible_numbers(numbers, divisor):
    return [num for num in numbers if is_divisible_by(num, divisor)]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_even_digit_sum_numbers(numbers):
    return [num for num in numbers if is_even(sum_of_digits(num))]

def find_odd_digit_sum_numbers(numbers):
    return [num for num in numbers if is_odd(sum_of_digits(num))]

def find_first_half_numbers(numbers, range_first, range_last):
    midpoint = (range_first + range_last) // 2
    return [num for num in numbers if num <= midpoint]

def find_second_half_numbers(numbers, range_first, range_last):
    midpoint = (range_first + range_last) // 2
    return [num for num in numbers if num > midpoint]

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def find_numbers_with_even_digital_root(numbers):
    return [num for num in numbers if digital_root(num) % 2 == 0]

def find_numbers_with_odd_digital_root(numbers):
    return [num for num in numbers if digital_root(num) % 2 != 0]

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

def find_perfect_square_numbers(numbers):
    return [num for num in numbers if is_perfect_square(num)]

def has_distinct_digits(n):
    return len(set(str(n))) == len(str(n))

def find_numbers_with_distinct_digits(numbers):
    return [num for num in numbers if has_distinct_digits(num)]

def ends_with_specific_digit(n, digit):
    return str(n)[-1] == str(digit)

def find_numbers_ending_with_digit(numbers, digit):
    return [num for num in numbers if ends_with_specific_digit(num, digit)]

def sum_of_digits_greater_than_threshold(n, threshold):
    return sum(int(digit) for digit in str(n)) > threshold

def find_numbers_with_sum_of_digits_greater_than_threshold(numbers, threshold):
    return [num for num in numbers if sum_of_digits_greater_than_threshold(num, threshold)]

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome_numbers(numbers):
    return [num for num in numbers if is_palindrome(num)]

def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    return (math.sqrt(5 * n ** 2 + 4) % 1 == 0) or (math.sqrt(5 * n ** 2 - 4) % 1 == 0)

def find_fibonacci_numbers(numbers):
    return [num for num in numbers if is_fibonacci(num)]

def is_power_of(n, base):
    if base == 1:
        return n == 1
    power = math.log(n) / math.log(base)
    return power.is_integer()

def find_power_of_numbers(numbers, base):
    return [num for num in numbers if is_power_of(num, base)]

def is_twin_prime(n):
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))

def find_twin_prime_numbers(numbers):
    return [num for num in numbers if is_twin_prime(num)]

def final_number(numbers):
    if len(numbers) == 1:
        print("The number is " + str(numbers[0]))
        time.sleep(10)
        quit()
    elif len(numbers) == 0:
        print("No possible numbers match the criteria.")
        quit()
    time.sleep(2)
    print("")

print("Welcome to the number game")
time.sleep(3)
print("I am Mystery Solver and i love to read the minds of peoples")
time.sleep(3)
print("Rules:")
print("You have think the number and it must be in the range you entered")
print("to say yes write 'y' and for no write 'n'")
print("All questions are compulsory")
print("fill only valid arguments which are suitable for fields")
print("")
time.sleep(10)
print("Game is Going to start now")
time.sleep(2)

range_of_numbers = input("Enter the range: ")
range_order = sort_numbers(range_of_numbers)
range_first_number = get_first_number(range_order)
range_last_number = get_last_number(range_order)

print(f"The range of numbers is {range_first_number} to {range_last_number}")
time.sleep(1)
print("Now I will ask you a few questions to read your mind")
time.sleep(2)
numbers = list(range(range_first_number, range_last_number + 1))

prime = input("Is the number prime? (y/n): ").lower()
if prime == "y":
    numbers = find_primes(numbers)
elif prime == "n":
    numbers = find_composites(numbers)
else:
    print("Invalid input")
    quit()

final_number(numbers)

while len(numbers) > 1:
    even = input("Is the number even? (y/n): ").lower()
    if even == "y":
        numbers = find_even_numbers(numbers)
    elif even == "n":
        numbers = find_odd_numbers(numbers)
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    divisible_by = input("Is the number divisible by 3? (y/n): ").lower()
    if divisible_by == "y":
        numbers = find_divisible_numbers(numbers, 3)
    elif divisible_by == "n":
        numbers = [num for num in numbers if not is_divisible_by(num, 3)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    digit_sum_even = input("Is the sum of the digits even? (y/n): ").lower()
    if digit_sum_even == "y":
        numbers = find_even_digit_sum_numbers(numbers)
    elif digit_sum_even == "n":
        numbers = find_odd_digit_sum_numbers(numbers)
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    half = input("Is the number in the first half of the range? (y/n): ").lower()
    if half == "y":
        numbers = find_first_half_numbers(numbers, range_first_number, range_last_number)
    elif half == "n":
        numbers = find_second_half_numbers(numbers, range_first_number, range_last_number)
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    perfect_square = input("Is the number a perfect square? (y/n): ").lower()
    if     perfect_square == "y":
        numbers = find_perfect_square_numbers(numbers)
    elif perfect_square == "n":
        numbers = [num for num in numbers if not is_perfect_square(num)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    distinct_digits = input("Does the number have distinct digits? (y/n): ").lower()
    if distinct_digits == "y":
        numbers = find_numbers_with_distinct_digits(numbers)
    elif distinct_digits == "n":
        numbers = [num for num in numbers if not has_distinct_digits(num)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    end_specific_digit = input("Does the number end with a specific digit? (y/n): ").lower()
    if end_specific_digit == "y":
        digit = int(input("Enter the digit (0-9): "))
        numbers = find_numbers_ending_with_digit(numbers, digit)
    elif end_specific_digit == "n":
        pass
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    sum_threshold = input("Is the sum of the digits greater than a threshold? (y/n): ").lower()
    if sum_threshold == "y":
        threshold = int(input("Enter the threshold: "))
        numbers = find_numbers_with_sum_of_digits_greater_than_threshold(numbers, threshold)
    elif sum_threshold == "n":
        pass
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    palindrome = input("Is the number a palindrome? (y/n): ").lower()
    if palindrome == "y":
        numbers = find_palindrome_numbers(numbers)
    elif palindrome == "n":
        numbers = [num for num in numbers if not is_palindrome(num)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    fibonacci = input("Is the number a Fibonacci number? (y/n): ").lower()
    if fibonacci == "y":
        numbers = find_fibonacci_numbers(numbers)
    elif fibonacci == "n":
        numbers = [num for num in numbers if not is_fibonacci(num)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    power_of = input("Is the number a power of a specific number? (y/n): ").lower()
    if power_of == "y":
        base = int(input("Enter the base: "))
        numbers = find_power_of_numbers(numbers, base)
    elif power_of == "n":
        pass
    else:
        print("Invalid input")
        quit()
    final_number(numbers)

    twin_prime = input("Is the number a twin prime? (y/n): ").lower()
    if twin_prime == "y":
        numbers = find_twin_prime_numbers(numbers)
    elif twin_prime == "n":
        numbers = [num for num in numbers if not is_twin_prime(num)]
    else:
        print("Invalid input")
        quit()
    final_number(numbers)
    time.sleep(2)

print("The number is " + str(numbers[0]))
