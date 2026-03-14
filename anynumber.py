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

    # full number range
    numbers = list(range(1, max_range + 1))

    # calculate n where 2^n >= max_range
    n = 1
    while 2 ** n < max_range:
        n += 1

    print(f"\nUsing random index array of size {n}")

    if max_range < n:
        print("Range too small.")
        return

    # random index array
    random_arr = sorted(random.sample(numbers, n))

    print("Random index array:")
    print(random_arr)

    # user number
    while True:
        target = int(input(f"\nPick a number between 1 and {max_range}: "))
        if 1 <= target <= max_range:
            break
        print("Number out of range. Try again.")

    print("\n--- Searching in random array first ---")

    # Direct check first - if target is in array, report immediately
    if target in random_arr:
        print(f"[Index] Found {target} in 1 guess!")
        return

    # If not found directly, do binary search to get bounds
    found, lower_bound, upper_bound = binary_search(random_arr, target, "[Index] ", return_bounds=True)

    print("\n--- Not found in index array. Searching full range ---")

    # Use bounds from first search to limit the second search
    if lower_bound is not None and upper_bound is not None:
        # Target is between lower_bound and upper_bound
        constrained_range = [x for x in numbers if lower_bound < x < upper_bound]
        print(f"Searching within bounds ({lower_bound}, {upper_bound}): {constrained_range}")
        if constrained_range:
            binary_search(constrained_range, target, "[Full Search] ")
        else:
            print(f"No numbers exist between {lower_bound} and {upper_bound}")
    elif lower_bound is not None:
        # Target is > lower_bound (upper bound is beyond array)
        constrained_range = [x for x in numbers if x > lower_bound]
        print(f"Searching above {lower_bound}: range size {len(constrained_range)}")
        binary_search(constrained_range, target, "[Full Search] ")
    elif upper_bound is not None:
        # Target is < upper_bound (lower bound is below array)
        constrained_range = [x for x in numbers if x < upper_bound]
        print(f"Searching below {upper_bound}: range size {len(constrained_range)}")
        binary_search(constrained_range, target, "[Full Search] ")
    else:
        # Shouldn't happen
        binary_search(numbers, target, "[Full Search] ")


if __name__ == "__main__":
    main()