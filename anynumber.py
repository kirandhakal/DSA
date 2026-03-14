import random


def binary_search(arr, target, label="", return_bounds=False):
    low = 0
    high = len(arr) - 1
    attempts = 0

    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            print(f"{label}Found {target} in {attempts} guesses!")
            return True if not return_bounds else (True, None, None)

        elif guess < target:
            print(f"{label}Attempt {attempts}: {guess} is too LOW")
            low = mid + 1

        else:
            print(f"{label}Attempt {attempts}: {guess} is too HIGH")
            high = mid - 1

    if return_bounds:
        # Return bounds based on what we learned from the search
        lower_bound = arr[high] if high >= 0 else None  # largest value < target
        upper_bound = arr[low] if low < len(arr) else None  # smallest value > target
        return False, lower_bound, upper_bound
    
    return False


def main():
    max_range = int(input("Enter the maximum range: "))
    numbers = list(range(1, max_range + 1))
    original_n = 1
    while 2 ** original_n < max_range:
        original_n += 1
    print(f"\nUsing random index array of size {original_n}")
    if max_range < original_n:
        print("Range too small.")
        return
    target = None
    while True:
        # Recalculate n for the current range
        current_range = len(numbers)
        n = 1
        while 2 ** n < current_range:
            n += 1
        random_arr = sorted(random.sample(numbers, n))
        print(f"Random index array:")
        print(random_arr)
        if target is None:
            target = int(input(f"\nPick a number between 1 and {max_range}: "))
        print("\n--- Searching in random array ---")
        if target in random_arr:
            print(f"[Index] Found {target} in 1 guess!")
            return
        found, lower_bound, upper_bound = binary_search(random_arr, target, "[Index] ", return_bounds=True)
        if found:
            return
        # Narrow bounds
        if lower_bound is not None and upper_bound is not None:
            numbers = [x for x in numbers if lower_bound < x < upper_bound]
            print(f"Narrowing to range ({lower_bound}, {upper_bound}): {numbers}")
        elif lower_bound is not None:
            numbers = [x for x in numbers if x > lower_bound]
            print(f"Narrowing to range above {lower_bound}: {numbers}")
        elif upper_bound is not None:
            numbers = [x for x in numbers if x < upper_bound]
            print(f"Narrowing to range below {upper_bound}: {numbers}")
        else:
            print("No bounds found, searching full range.")
        if len(numbers) == 0:
            print("Target not found in any narrowed range.")
            return


if __name__ == "__main__":
    main()