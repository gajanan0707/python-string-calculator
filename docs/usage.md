# String Calculator Usage Guide

## Basic Usage

The String Calculator provides a simple interface for adding numbers in a string format:

```python
from string_calculator import add

# Add numbers separated by commas
result = add("1,2,3")  # Returns 6

# Add numbers separated by newlines
result = add("1\n2\n3")  # Returns 6

# Mix of commas and newlines
result = add("1\n2,3")  # Returns 6
```

## Custom Delimiters

You can specify custom delimiters using the `//[delimiter]\n` format:

```python
# Single character delimiter
result = add("//;\n1;2;3")  # Returns 6

# Multi-character delimiter
result = add("//[***]\n1***2***3")  # Returns 6
```

## Error Handling

The calculator provides clear error messages for invalid inputs:

```python
# Negative numbers
try:
    add("-1,2,-3")
except ValueError as e:
    print(e)  # "negative numbers not allowed: -1, -3"

# Invalid format
try:
    add("1,2,")
except ValueError as e:
    print(e)  # "invalid number format"

# Empty delimiter
try:
    add("//\n1,2")
except ValueError as e:
    print(e)  # "empty delimiter not allowed"
```

## Best Practices

1. Always handle exceptions when using the calculator
2. Use consistent delimiters in your input strings
3. Consider using custom delimiters for complex number formats
4. Test your code with various input formats

## Examples

### Basic Addition
```python
result = add("1,2,3,4,5")  # Returns 15
```

### Mixed Delimiters
```python
result = add("1\n2,3\n4,5")  # Returns 15
```

### Custom Delimiter
```python
result = add("//|\n1|2|3|4|5")  # Returns 15
```

### Complex Custom Delimiter
```python
result = add("//[***]\n1***2***3***4***5")  # Returns 15
``` 