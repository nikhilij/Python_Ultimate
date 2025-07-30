def print_histogram_vertical(histogram):
    keys = sorted(histogram)
    counts = [histogram[k] for k in keys]
    max_count = max(counts)

    # Print histogram bars
    for level in range(max_count, 0, -1):
        line = "│"
        for count in counts:
            line += " █ " if count >= level else "   "
        print(line)
    # Print separator
    print("└" + "───" * len(keys))
    # Print keys as labels
    print(" ".join(f"{k:^3}" for k in keys))

def create_histogram(numbers):
    histogram = {}
    for num in numbers:
        histogram[num] = histogram.get(num, 0) + 1
    return histogram

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    histogram = create_histogram(numbers)
    print_histogram_vertical(histogram)
