def count_words(text):
    words_array = text.split()
    return len(words_array)

def count_chars(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict    

def get_sorted_list(chars_dict):
    dict_list = []
    for char in chars_dict:
        dict_list.append({"char": char,"num": chars_dict[char]})     

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]
