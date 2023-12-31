from collections import Counter


class UniqueCharacterCounter:
    def __init__(self) -> None:
        self.cache = {}

    def count_unique_characters(self, input_string: str) -> int:
        if input_string in self.cache:
            return self.cache[input_string]

        unique_count = len(Counter(input_string))

        self.cache[input_string] = unique_count

        return unique_count
