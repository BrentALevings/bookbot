def count_words(book_text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        book_text (str): The text extracted from the book.

    Returns:
        word_count (int): The number of words
    """

    return len(book_text.split())

def count_chars(book_text: str) -> dict[str, int]:
    """
    Count the number of times a character appears in a string.

    Args:
        book_text (str): The text extracted from the book.

    Returns:
        char_counts (dict[str, int]): A dictionary object of each char and its count
    """

    char_counts = {}
    for char in book_text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1
    
    return char_counts

def sort_dict(unsorted_dict: dict[str, int]) -> list[dict[str, int]]:
    sorted_list = []

    for item in unsorted_dict:
        sorted_list.append({"char": item, "num": unsorted_dict[item]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(items):
    return items["num"]