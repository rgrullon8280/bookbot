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
