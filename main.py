from stats import get_num_words
from stats import get_char_count
def get_book_text(file) :
    file_string = file.read()
    return file_string


file_path = 'books/frankenstein.txt'

def main():
    
    with open(file_path) as file :
        text_string = get_book_text(file)
        num_words = get_num_words(text_string)
        print(f'{num_words} words found in the document')
        
        num_chars = get_char_count(text_string)
        print(num_chars)

main()

