from stats import get_num_words, count_chars, chars_dict_to_sorted_list
import sys


def get_book_text(path: str) -> None:
    with open(path) as f:
        return f.read()    

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    counter = count_chars(get_book_text(sys.argv[1]))
    print_report(sys.argv[1], get_num_words(get_book_text(sys.argv[1])), chars_dict_to_sorted_list(counter))

def print_report(path: str, word_count: int, counter: list[tuple[str: int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in counter:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")


main()