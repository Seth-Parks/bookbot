from stats import get_num_words
from stats import get_char_count
from stats import sort_char_dict
import sys


#Function to read file
def get_book_text(file) :
    file_string = file.read()
    return file_string


def main():
    #Checking system arguments
    if(len(sys.argv) != 2):
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

    file_path = sys.argv[1]

    text_string = None

    with open(file_path) as file :
        #Opening file and reading in text as a string
        text_string = get_book_text(file)


    #Processing 
    num_words = get_num_words(text_string)
    num_chars = get_char_count(text_string)
    sorted_list = sort_char_dict(num_chars)
    
    #Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #Only prints the character if the character is alphabetical
    for item in sorted_list:
        if(item['char'].isalpha()):
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


        
        
    


main()

