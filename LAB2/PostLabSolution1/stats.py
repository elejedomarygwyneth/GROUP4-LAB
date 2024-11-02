def mean(numbers):
    """Calculate the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes  

def main():
    """Main function to test the statistical functions."""
    sample_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Sample numbers: {sample_numbers}")
    print(f"Mean: {mean(sample_numbers)}")
    print(f"Median: {median(sample_numbers)}")
    print(f"Mode: {mode(sample_numbers)}")

if __name__ == "__main__":
    main()

