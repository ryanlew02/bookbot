#prints number of total words in string
from typing import Counter


def get_num_words(string: str) -> None:
    print(f"Found {len(string.split())} total words")

def count_chars(string: str) -> dict[str: int]:
    return Counter(string.lower())

def sort_on(tup: tuple[str, int]) -> int:
    return tup[1]

def chars_dict_to_sorted_list(dic: dict[str, int]) -> list[tuple[str: int]]:
    tuple_list = []

    for key, value in dic.items():
        tuple_list.append((key, value))
    
    sorted_list = sorted(tuple_list, reverse=True, key=sort_on)

    return sorted_list