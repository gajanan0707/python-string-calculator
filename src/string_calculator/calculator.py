"""
String Calculator Module

This module provides functionality to add numbers in a string using various delimiters.
"""

from typing import List, Tuple


class StringCalculator:
    """A calculator that adds numbers from a string with various delimiters."""

    def __init__(self):
        """Initialize the calculator with default settings."""
        self.default_delimiter = ","
    
    def _parse_custom_delimiter(self, numbers: str) -> Tuple[str, str]:
        """
        Extract custom delimiter and remaining numbers from input string.
        
        Args:
            numbers: Input string containing numbers and optional delimiter specification.
            
        Returns:
            Tuple containing the delimiter and the remaining numbers string.
            
        Raises:
            ValueError: If the delimiter format is invalid or empty.
        """
        if not numbers.startswith("//"):
            return self.default_delimiter, numbers
            
        delimiter_end = numbers.find("\n")
        if delimiter_end == -1:
            raise ValueError("invalid format: missing newline after delimiter")
        
        delimiter = numbers[2:delimiter_end]
        if not delimiter:
            raise ValueError("empty delimiter not allowed")
            
        # Handle bracketed delimiters
        if delimiter.startswith("[") and delimiter.endswith("]"):
            delimiter = delimiter[1:-1]
            
        return delimiter, numbers[delimiter_end + 1:]
    
    def _split_numbers(self, numbers: str, delimiter: str) -> List[str]:
        """
        Split input string into list of number strings.
        
        Args:
            numbers: String containing numbers separated by delimiters.
            delimiter: The delimiter to use for splitting.
            
        Returns:
            List of number strings.
        """
        # Replace newlines with delimiter
        numbers = numbers.replace("\n", delimiter)
        
        # For multi-character delimiters, we need to handle them specially
        if len(delimiter) > 1:
            parts = []
            while numbers:
                if numbers.startswith(delimiter):
                    numbers = numbers[len(delimiter):]
                    continue
                next_delim = numbers.find(delimiter)
                if next_delim == -1:
                    parts.append(numbers)
                    break
                parts.append(numbers[:next_delim])
                numbers = numbers[next_delim:]
            return [part.strip() for part in parts if part.strip()]
        
        return [num.strip() for num in numbers.split(delimiter)]
    
    def _validate_and_parse_numbers(self, number_strings: List[str]) -> List[int]:
        """
        Validate and convert string numbers to integers.
        
        Args:
            number_strings: List of strings representing numbers.
            
        Returns:
            List of integers.
            
        Raises:
            ValueError: If any string is empty or not a valid number.
        """
        # Check for empty strings
        if not all(number_strings) or "" in number_strings:
            raise ValueError("invalid number format")
        
        try:
            return [int(num) for num in number_strings]
        except ValueError:
            raise ValueError("invalid number format")
    
    def _check_negatives(self, numbers: List[int]) -> None:
        """
        Check for negative numbers and raise exception if found.
        
        Args:
            numbers: List of numbers to check.
            
        Raises:
            ValueError: If any negative numbers are found.
        """
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")


def add(numbers: str) -> int:
    """
    Add numbers in a string using various delimiters.
    
    Args:
        numbers: String containing numbers separated by delimiters.
                Can include custom delimiter specification at the start.
                
    Returns:
        The sum of the numbers.
        
    Raises:
        ValueError: If the input format is invalid or contains negative numbers.
    """
    if not numbers:
        return 0
        
    calculator = StringCalculator()
    
    # Parse custom delimiter if present
    delimiter, numbers = calculator._parse_custom_delimiter(numbers)
    
    # Split into number strings
    number_strings = calculator._split_numbers(numbers, delimiter)
    
    # Convert to integers
    nums = calculator._validate_and_parse_numbers(number_strings)
    
    # Check for negatives
    calculator._check_negatives(nums)
    
    return sum(nums) 