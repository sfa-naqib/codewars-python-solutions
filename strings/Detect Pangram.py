import string
def is_pangram(st):
    alphabet = list(string.ascii_lowercase)
    for i in alphabet:
        if i in st.lower():
            continue
        else:
            return False
    return True
