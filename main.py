import sys
from stats import count, repeat_char, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main(filepath):
    text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count(text)} total words")

    print("--------- Character Count -------")
    char_count = repeat_char(text)
    sorted_char_count = sort_char_counts(char_count)

    for char, num in sorted_char_count:
        if char in [" ", "\n", "\t"]:
            continue
        print(f"{char}: {num}")

# --- CLI handling ---
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
main(filepath)
