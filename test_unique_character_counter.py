from collections import Counter


class UniqueCharacterCounter:
    def __init__(self):
        # Cache to store results for previously encountered strings
        self.cache = {}

    def count_unique_characters(self, input_string):
        if input_string in self.cache:
            # Retrieve the result from the cache
            return self.cache[input_string]

        # Count unique characters using Counter
        unique_count = len(Counter(input_string))

        # Cache the result for future use
        self.cache[input_string] = unique_count

        return unique_count


# Tests using pytest
def test_count_unique_characters():
    counter = UniqueCharacterCounter()

    # Test 1
    result1 = counter.count_unique_characters("abcde")
    assert result1 == 5

    # Test 2 (using the same string as before)
    result2 = counter.count_unique_characters("abcde")
    assert result2 == 5

    # Test 3 (new string)
    result3 = counter.count_unique_characters("aabbc")
    assert result3 == 3

# Run the tests with pytest
# Save this code in a file (e.g., test_unique_character_counter.py) and run:
# pytest test_unique_character_counter.py
