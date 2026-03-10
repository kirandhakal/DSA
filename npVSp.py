// Function to generate primes up to n using Sieve of Eratosthenes
function get_primes(n):
    initialize sieve as array of true values, size n+1
    for p from 2 to sqrt(n) + 1:
        if sieve[p] is true:
            for i from p*p to n step p:
                set sieve[i] to false
    primes = empty list
    for p from 2 to n:
        if sieve[p] is true:
            add p to primes
    return primes

// Optimal guessing function using binary search
function optimal_prime_guess(target, max_range):
    primes = get_primes(max_range)
    low = 0
    high = length of primes - 1
    attempts = 0
    
    output "Searching within " + length of primes + " possible primes..."
    
    while low <= high:
        attempts = attempts + 1
        mid_idx = floor((low + high) / 2)
        guess = primes[mid_idx]
        
        if guess == target:
            return "Found " + target + " in " + attempts + " guesses!"
        else if guess < target:
            output "Attempt " + attempts + ": " + guess + " is too LOW"
            low = mid_idx + 1
        else:
            output "Attempt " + attempts + ": " + guess + " is too HIGH"
            high = mid_idx - 1
    
    return "Number not found in prime list."