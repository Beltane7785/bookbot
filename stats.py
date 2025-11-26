def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def get_counts(character_counts):
    pass

def sort_counts(character_counts):
    sorted_list = []
    for key in character_counts:
        sorted_list.append({"char": key, "num": character_counts[key]})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list