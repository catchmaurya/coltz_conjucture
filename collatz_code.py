
# collatz_code.py

collatz_cache = {}

def collatz_path(n):
    """Returns the Collatz path for a given number n, using memoization."""
    if n in collatz_cache:
        return collatz_cache[n]

    original_n = n
    path = []
    while n != 1:
        path.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in collatz_cache:
            path.extend(collatz_cache[n][1:])  # skip repeated head
            break

    path.append(1)
    collatz_cache[original_n] = path
    return path

def collatz_step_count(n):
    """Returns the number of steps to reach 1 from n."""
    return len(collatz_path(n)) - 1

def generate_collatz_data(start, end):
    """Generates Collatz steps for numbers from start to end."""
    result = []
    for i in range(start, end + 1):
        steps = collatz_step_count(i)
        path = collatz_path(i)
        result.append((i, steps, path))
    return result

if __name__ == "__main__":
    import csv

    data = generate_collatz_data(1, 100)
    with open("example_output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Number", "Steps", "Path"])
        for num, steps, path in data:
            writer.writerow([num, steps, path])
    print("Collatz data for 1–100 saved to example_output.csv")
