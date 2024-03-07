def main():
    book_path = "/home/arctor/workspace/github.com/C-Bashaw/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"words: {num_words} ")
    print(num_letters)

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
    return {k: letters[k] for k in sorted(letters)}


main()