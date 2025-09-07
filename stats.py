def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    character_count = {}
    
    for char in book_text:
        low_char = char.lower()
        if low_char in character_count:
            character_count[low_char] += 1
        else:
            character_count[low_char] = 1
    return character_count

def get_sorted_character_count(character_count):
    count_list = []
    for char in character_count:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = character_count[char]
        count_list.append(char_dict)
        
    count_list.sort(key=lambda c: c["num"], reverse=True)
    return count_list
