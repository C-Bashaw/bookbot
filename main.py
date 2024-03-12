def main():
    book_path = "/home/arctor/workspace/github.com/C-Bashaw/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"Begin Report")
    print(f"{num_words} words found in the document")
    for letter in num_letters:
        print(f"The {letter['char']} character was found {letter['count']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    letters = {}
    lower_text = text.lower()
    for c in lower_text:
        if c.isalpha():
            letters[c] = (letters.get(c, 0)) + 1
    list_of_letters = []
    for l, count in letters.items():
        new_list = {'char': l, 'count': count}
        list_of_letters.append(new_list)
    list_of_letters.sort(reverse=True, key=get_count)
    return list_of_letters

def get_count(letters):
    return letters['count']

main()