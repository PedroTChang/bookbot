def main():
    book_path = "books/frankenstein.txt"

    # Print header
    print(f"--- Begin report of {book_path} ---")

    # Get and print word count
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")

    # Get character count and convert to sorted list
    char_counts = count_characters(text)
    char_list = convert_to_list(char_counts)

    # Print each character count
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' was found {char_dict['num']}'")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def count_characters(text):
    characters = {}
    lower_text = text.lower()
    for x in lower_text:
        if x in characters:
            characters[x] += 1
        else:
            characters[x] = 1
    return characters


def sort_on(dict):
    return dict["num"]


def convert_to_list(characters):
    alpha = [
        {"char": key, "num": value}
        for key, value in characters.items()
        if key.isalpha()
    ]
    alpha.sort(reverse=True, key=sort_on)
    return alpha


if __name__ == "__main__":
    main()
