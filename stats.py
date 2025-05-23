def get_num_words(text_string):
    #splits the text_string into text_list by whitespace, allowing us to 
    #return the length of the list (or the total word count)
    text_list = text_string.split()
    return len(text_list)

def get_char_count(text_string):
    #Declare the a dictonary of characters, where the key is a 
    #character and the value is the count in the string
    char_dict = {}
    #iterate through each character in the string
    for char in text_string:
        #assume we haven't seen the character before
        has_char = False
        #convert the char to lowercase
        char = char.lower()
        #check to see if the character is already in the dictionary
        for key in char_dict:
            if(key == char):
                has_char = True

        #if the character is found, then we want to increment it        
        if(has_char):
            char_dict[char] += 1
        else:
            #otherwise, we want to assign a new value for it and 
            #store the new value at 1
            char_dict[char] = 1

    return char_dict


def sort_on(dict):
    return dict['num']


def sort_char_dict(char_dict):
    #In order to sort the dict, we need to first move it into a list
    sorted_list = []
    #for each item in the original dict, we want to add new information and
    #store it in a list to be sorted
    for key, value in char_dict.items():
        new_dict = {'char': key, 'num': value}
        sorted_list.append(new_dict)
    
    #sort the list
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list