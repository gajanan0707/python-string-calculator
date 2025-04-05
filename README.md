# String Calculator

A Python implementation of the String Calculator kata following Test-Driven Development (TDD) practices.

## Features

- Handles empty strings (returns 0)
- Handles single numbers
- Handles multiple numbers with comma delimiters
- Supports newlines between numbers
- Supports custom delimiters
- Throws appropriate exceptions for negative numbers
- Includes all negative numbers in the exception message

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/string-calculator.git
cd string-calculator

# Install dependencies
pip install -r requirements.txt
```

## Usage

```python
from string_calculator import add

# Basic usage
result = add("1,2,3")  # Returns 6

# With newlines
result = add("1\n2,3")  # Returns 6

# With custom delimiter
result = add("//;\n1;2")  # Returns 3

# With multi-character delimiter
result = add("//[***]\n1***2***3")  # Returns 6
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src.string_calculator
```

### Code Quality

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Type checking
mypy src
```

## Project Structure

```
string-calculator/
├── src/
│   └── string_calculator/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_calculator.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.