import sys

from stats import count_words, count_chars, sort_dict

def get_book_text(filepath: str) -> str:
    """
    Method to get book text

    Args:
        filepath (str): The filepath to the book text

    Returns:
        book_text (str): The book text
    """

    with open(filepath, "r") as f:
        book_text = f.read()

    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"Found {count_words(get_book_text(book_path))} total words")

    char_counts = count_chars(get_book_text(book_path))

    sorted_chars = sort_dict(char_counts)
    for sorted_char in sorted_chars:
        if sorted_char["char"] == " ":
            continue
        print(f"{sorted_char['char']}: {sorted_char['num']}")

main()