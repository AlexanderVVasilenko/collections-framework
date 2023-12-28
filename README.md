# package_vas1505

The `package_vas1505` package is a Python module that includes the `UniqueCharacterCounter` class. This class is designed to efficiently count the number of unique characters in a given string while incorporating a caching mechanism for optimized performance.

## Installation

Clone the repository and include the `package_vas1505` directory in your project. Import the `UniqueCharacterCounter` class to start using the unique character counting functionality.

```python
from package_vas1505.unique_character_counter import UniqueCharacterCounter

# Create an instance of UniqueCharacterCounter
counter = UniqueCharacterCounter()

# Count unique characters in a string
result = counter.count_unique_characters("abcde")
print(f"Number of unique characters: {result}")
