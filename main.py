def main():
    book_path = "books/frankenstein.txt"
    file_contents = extract_book_text(book_path)
    num_words = count_words(file_contents)
    char_dict = extract_characters_dict(file_contents)
    sorted_list = convert_dict_to_list(char_dict)
    print_report(book_path, num_words, sorted_list)

def extract_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)    

def extract_characters_dict(text):
    char_dict = {}
    for c in text:
        lc = c.lower()
        if lc in char_dict:
            char_dict[lc] += 1
        else:
            char_dict[lc] = 1
    return char_dict

def convert_dict_to_list(char_dict):
    list = []
    for key in char_dict:
        list.append({"char": key, "count": char_dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]

def print_report(book_path, word_count, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for item in char_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

main()

