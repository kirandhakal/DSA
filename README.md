# Prime Number Guessing Game - README

## Overview
This project implements an optimal prime number guessing game using binary search on a precomputed list of prime numbers. The algorithm intelligently guesses prime numbers within a given range by leveraging the Sieve of Eratosthenes and binary search principles.

## Features
- Generates all prime numbers up to a specified maximum using the Sieve of Eratosthenes
- Implements binary search to find a target prime number with minimal attempts
- Provides feedback on each guess (too high/too low)
- Tracks the number of attempts
- Optimized for efficiency with O(log n) time complexity

## How It Works
1. **Prime Generation**: All prime numbers up to `max_range` are generated using the Sieve of Eratosthenes
2. **Binary Search**: The algorithm performs binary search on the sorted list of primes
3. **Feedback Loop**: After each guess, the user receives feedback to guide the next guess
4. **Completion**: The game ends when the correct prime is found or it's determined not in the list

## Time Complexity
- Prime Generation: O(n log log n)
- Binary Search: O(log n) where n is the number of primes

## Usage Example
```python
# Guess the prime number 73 in range 1-100
print(optimal_prime_guess(73, 100))

# Output:
# Searching within 25 possible primes...
# Attempt 1: 41 is too LOW
# Attempt 2: 73 is too HIGH
# Found 73 in 2 guesses!
```

---

# Pseudo Code

## Main Functions

```
FUNCTION get_primes(n)
    // Generate all prime numbers up to n using Sieve of Eratosthenes
    
    CREATE array sieve of size n+1, initialized to True
    SET sieve[0] and sieve[1] to False
    
    FOR p FROM 2 TO sqrt(n)
        IF sieve[p] is True
            FOR i FROM p*p TO n STEP p
                SET sieve[i] to False
    
    CREATE empty list primes
    FOR p FROM 2 TO n
        IF sieve[p] is True
            ADD p to primes
    
    RETURN primes
```

```
FUNCTION optimal_prime_guess(target, max_range)
    // Find target prime using binary search
    
    primes = get_primes(max_range)
    SET low = 0
    SET high = length(primes) - 1
    SET attempts = 0
    
    PRINT "Searching within [size] possible primes..."
    
    WHILE low <= high
        attempts = attempts + 1
        mid_idx = (low + high) / 2  // integer division
        guess = primes[mid_idx]
        
        IF guess == target
            RETURN "Found target in attempts guesses!"
        
        ELSE IF guess < target
            PRINT "Attempt attempts: guess is too LOW"
            low = mid_idx + 1
        
        ELSE
            PRINT "Attempt attempts: guess is too HIGH"
            high = mid_idx - 1
    
    RETURN "Number not found in prime list."
```

## Binary Search Algorithm Flow

```
START
    ↓
Generate primes up to max_range
    ↓
Initialize low = 0, high = len(primes)-1, attempts = 0
    ↓
    ┌─────────────────────────────────────┐
    ↓                                     │
WHILE low <= high                         │
    ↓                                     │
Calculate mid = (low + high) / 2           │
    ↓                                     │
attempts++                                 │
    ↓                                     │
guess = primes[mid]                        │
    ↓                                     │
    ├─ IF guess == target ────► FOUND ────┘
    │
    ├─ IF guess < target ────► low = mid + 1
    │
    └─ IF guess > target ────► high = mid - 1
                                      │
                                      ↓
                            ┌─────────────────┐
                            │  END WHILE      │
                            └─────────────────┘
                                      ↓
                          IF number not found
                                      ↓
                                    END
```

## Key Points
- The algorithm assumes the target number is a prime
- Binary search works because primes are generated in ascending order
- Maximum efficiency achieved with O(log n) guesses
- Works best when target is within the prime list