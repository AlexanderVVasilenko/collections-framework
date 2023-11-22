import argparse
from typing import Callable

from test_unique_character_counter import UniqueCharacterCounter


def main(count_characters: Callable) -> None:
    parser = argparse.ArgumentParser(description="Count the number of unique characters in a string or file.")
    parser.add_argument('--string', help='Input string to count unique characters.')
    parser.add_argument('--file', help='Path to a text file to process.')

    args = parser.parse_args()

    if args.string:
        result = count_characters(args.string)
        print(f"Number of unique characters in the string: {result}")

    elif args.file:
        try:
            with open(args.file, 'r') as file:
                file_content = file.read()
                result = count_characters(file_content)
                print(f"Number of unique characters in the file: {result}")

        except FileNotFoundError:
            print(f"Error: File not found - {args.file}")


if __name__ == '__main__':
    unique_character_counter = UniqueCharacterCounter()
    main(unique_character_counter.count_unique_characters)