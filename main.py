from stats import get_num_words
from stats import get_char_count
from stats import sort_char_dict

def get_book_text(file) :
    file_string = file.read()
    return file_string




file_path = 'books/frankenstein.txt'

def main():
    
    with open(file_path) as file :
        #Processimg
        text_string = get_book_text(file)
        num_words = get_num_words(text_string)
        num_chars = get_char_count(text_string)
        sorted_list = sort_char_dict(num_chars)
        
        #Output
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for item in sorted_list:
            if(item['char'].isalpha()):
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")


        
        
    


main()

