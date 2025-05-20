

def get_book_text(file) :
    file_string = file.read()
    return file_string


def print_words_in_text(text_string):
    text_list = text_string.split()
    return len(text_list)

file_path = 'books/frankenstein.txt'

def main():
    
    with open(file_path) as file :
        text_string = get_book_text(file)
        num_words = print_words_in_text(text_string)
        print(f'{num_words} words found in the document')
        

main()

