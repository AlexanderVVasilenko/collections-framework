from src.package_vas1505.unique_character_counter import UniqueCharacterCounter


def test_count_unique_characters() -> None:
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
# pytest tests\test_unique_character_counter.py
