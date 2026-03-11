def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

import math
import random

def get_primes(n):
    """Generates a list of primes up to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def guess_number_flow():
    # 1. Ask for range
    max_range = int(input("Enter the maximum range: "))
    # 2. Calculate n such that 2^n >= max_range
    n = 1
    while 2 ** n < max_range:
        n += 1
    print(f"For range {max_range}, using array of {n} random numbers.")
    # 3. Generate array of n random numbers
    arr = sorted(random.sample(range(1, max_range + 1), n))
    print(f"Random array: {arr}")
    # 4. Ask user for a number
    user_num = int(input(f"Pick a number between 1 and {max_range}: "))
    # 5. Guessing algorithm (binary search style)
    low = 0
    high = n - 1
    attempts = 0
    found = False
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        guess = arr[mid]
        print(f"Attempt {attempts}: Guessing {guess}")
        if guess == user_num:
            print(f"Found your number {user_num} in {attempts} guesses!")
            found = True
            break
        elif guess < user_num:
            print(f"{guess} is too LOW")
            low = mid + 1
        else:
            print(f"{guess} is too HIGH")
            high = mid - 1
    if not found:
        print(f"Your number {user_num} was not in the array. Closest guess in {attempts} attempts.")


# Run the flow if this file is executed directly
if __name__ == "__main__":
    guess_number_flow()

def optimal_prime_guess(target, max_range):
    primes = get_primes(max_range)
    low = 0
    high = len(primes) - 1
    attempts = 0

    print(f"Searching within {len(primes)} possible primes...")

    while low <= high:
        attempts += 1
        mid_idx = (low + high) // 2
        guess = primes[mid_idx]

        if guess == target:
            return f"Found {target} in {attempts} guesses!"
        elif guess < target:
            print(f"Attempt {attempts}: {guess} is too LOW")
            low = mid_idx + 1
        else:
            print(f"Attempt {attempts}: {guess} is too HIGH")
            high = mid_idx - 1

    return "Number not found in prime list."
if __name__ == "__main__":
    while True:
        target = int(input("Enter the prime number to search for: "))
        if is_prime(target):
            break
        else:
            print(f"{target} is NOT a prime number. Please enter a prime number.")
    max_range = int(input("Enter the maximum range: "))
    print(optimal_prime_guess(target, max_range))