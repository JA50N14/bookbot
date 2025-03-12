def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count


def get_character_count(book_text):
    char_dict = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in char_dict:
            char_dict[char_lower] += 1
        else:
            char_dict[char_lower] = 1
    return char_dict


def sort_on(dict):
    return dict['num']


def sorted_list_of_chars(char_dict):
    sorted_lst = []
    for k, v in char_dict.items():
        sorted_lst.append({'char': k, 'num': v})

    sorted_lst.sort(key=sort_on, reverse=True)
    return sorted_lst

