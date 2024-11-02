def mean(numbers):
    """Calculate the average of a list of numbers."""
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
    else:  
        return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return None
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    return modes[0] if modes else None
