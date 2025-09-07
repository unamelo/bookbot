from stats import get_num_words, get_num_characters, get_sorted_character_count
import sys

def main():

    # Get the argument from the command line
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = arguments[1]

    book_text = get_book_text(path_to_file)
    word_count = get_num_words(book_text)
    character_count = get_num_characters(book_text)
    sorted_character_count = get_sorted_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char in sorted_character_count:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents




if __name__ == "__main__":
    main()


