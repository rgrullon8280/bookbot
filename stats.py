def get_num_words(string):
    return len(string.split())

def get_character_count(string):
    count_dict = {}
    for char in string:
        char_lower = char.lower()
        if char_lower in count_dict:
            count_dict[char_lower] += 1
        else:
            count_dict[char_lower] = 1
    return count_dict

def get_sorted_char_counts(char_dict):
    # pythonic way
    # char_dict_list = [{'character': key, 'count': value} for key, value in char_dict.items() if key.isalpha()]
    # Normal way
    char_dict_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_dict_list.append(
                {
                    'character': char,
                    'count': count
                }
            )
    sorted_char_dict_list = sorted(char_dict_list, key=lambda x: x['count'], reverse=True)
    return(sorted_char_dict_list)
