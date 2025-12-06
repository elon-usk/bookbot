def count(text):
    words = text.split()
    return len(words)

def repeat_char(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_char_counts(char_count):
    return sorted(char_count.items(),key=lambda item: item[1], reverse=True)