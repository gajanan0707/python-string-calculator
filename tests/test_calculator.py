"""
Test module for the String Calculator.

This module contains all the test cases for the String Calculator implementation,
following Test-Driven Development (TDD) practices.
"""

import pytest
from src.string_calculator import add


class TestBasicFunctionality:
    """Test cases for basic calculator functionality."""
    
    def test_empty_string_returns_zero(self):
        """Empty string should return 0."""
        assert add("") == 0
    
    def test_single_number_returns_value(self):
        """Single number should return its value."""
        assert add("1") == 1
        assert add("5") == 5
    
    def test_two_numbers_returns_sum(self):
        """Two numbers should return their sum."""
        assert add("1,2") == 3
        assert add("3,5") == 8


class TestMultipleNumbers:
    """Test cases for handling multiple numbers."""
    
    def test_multiple_numbers_returns_sum(self):
        """Multiple numbers should return their sum."""
        assert add("1,2,3") == 6
        assert add("1,2,3,4,5") == 15


class TestNewlineDelimiter:
    """Test cases for newline as a delimiter."""
    
    def test_newline_as_valid_delimiter(self):
        """Newlines should be valid delimiters."""
        assert add("1\n2") == 3
        assert add("1\n2,3") == 6
        assert add("1,2\n3") == 6


class TestCustomDelimiter:
    """Test cases for custom delimiters."""
    
    def test_custom_single_character_delimiter(self):
        """Single character custom delimiters should work."""
        assert add("//;\n1;2") == 3
        assert add("//|\n1|2|3") == 6
    
    def test_custom_multi_character_delimiter(self):
        """Multi-character custom delimiters should work."""
        assert add("//sep\n1sep2sep3") == 6
        assert add("//[***]\n1***2***3") == 6


class TestInputValidation:
    """Test cases for input validation."""
    
    def test_rejects_negative_numbers(self):
        """Negative numbers should raise an exception."""
        with pytest.raises(ValueError) as exc:
            add("-1,2")
        assert str(exc.value) == "negative numbers not allowed: -1"
        
        with pytest.raises(ValueError) as exc:
            add("2,-4,3,-5")
        assert str(exc.value) == "negative numbers not allowed: -4, -5"
    
    def test_handles_whitespace(self):
        """Whitespace should be handled properly."""
        assert add("1, 2, 3") == 6
        assert add(" 1 , 2 , 3 ") == 6
    
    def test_rejects_invalid_input(self):
        """Invalid input formats should raise appropriate exceptions."""
        invalid_inputs = [
            ("//\n1,2", "empty delimiter not allowed"),
            ("1,2,", "invalid number format"),
            ("1,a,2", "invalid number format"),
            ("1,2\n", "invalid number format"),
            ("//;\n1;", "invalid number format"),
        ]
        
        for invalid_input, expected_error in invalid_inputs:
            with pytest.raises(ValueError) as exc:
                add(invalid_input)
            assert str(exc.value) == expected_error 