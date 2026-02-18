import re
def to_camel_case(text):
    delimiters = r"[_-]"
    word_list = re.split(delimiters,text)
    camel_list = [word[0].upper()+word[1:] for word in word_list if word_list.index(word) != 0]
    camel_list = list(word_list[0])+camel_list
    return ''.join(camel_list)
