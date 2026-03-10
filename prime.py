def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
import math

def get_primes(n):
    """Generates a list of primes up to n using Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [p for p in range(2, n + 1) if sieve[p]]

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
            # print(f"{target} is a prime number.")
            break
        else:
            print(f"{target} is NOT a prime number. Please enter a prime number.")
    max_range = int(input("Enter the maximum range: "))
    print(optimal_prime_guess(target, max_range))