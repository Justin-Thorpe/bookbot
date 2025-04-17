def word_count(text):
    wordcount = len(text.split())
    return wordcount
    
def letter_count(text):
    characters = set(text.lower())
    char_dict = dict.fromkeys(characters, 0)
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
    
    return char_dict

def dict_sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list