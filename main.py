from stats import get_num_words, get_character_count, sorted_list_of_chars
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        return sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    word_count = get_num_words(file_content)
    char_count_dict = get_character_count(file_content)
    sorted_lst = sorted_list_of_chars(char_count_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    
    for items in sorted_lst:
        if items['char'].isalpha():
            print(f'{items['char']}: {items['num']}')
    
    print('============= END ===============')

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()