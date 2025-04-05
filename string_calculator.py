def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Handle custom delimiter
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_end = numbers.find("\n")
        delimiter = numbers[2:delimiter_end]
        numbers = numbers[delimiter_end + 1:]

    # Replace newlines with the delimiter
    numbers = numbers.replace("\n", delimiter)
    
    # Split and convert to integers
    nums = [int(num) for num in numbers.split(delimiter)]
    
    # Check for negative numbers
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(nums) 