import string

# List of "unimportant" words that should be filtered out
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'do', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'will', 'would']

# Removes words from "unimportant" list and returns a filtered list of words
def filter_words(words, skip_words):
    important_words = list()

    for current_str in words:
        if not current_str in skip_words:              # Check if the current word is not in the list of "unimportant" words
            important_words.append(current_str)        # If it's not in the skip_words list, add it to the important_words list

    return important_words

# Removes punctuation from input string
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

# Removes spaces between words and splits string into a list of words
def remove_spaces(text):
    no_spaces = list()
    
    no_spaces_buffered = text.split(' ')
    for str in no_spaces_buffered:              # Iterate through the buffered list of words and Check if the current word is not an empty string
        if not str == "":                       # If it's not empty, add it to the no_spaces list
            no_spaces.append(str)

    return no_spaces

# Takes input and returns filtered list of important words
def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()

    # Remove whitespace & split words
    no_spaces_list = remove_spaces(no_punct)

    # Remove unimportant words
    important_words = filter_words(no_spaces_list, skip_words) 

    return important_words
