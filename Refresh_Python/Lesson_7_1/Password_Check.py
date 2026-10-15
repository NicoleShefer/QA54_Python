import re

def has_digits(password):
    return bool(re.search(r"\d",password))

print(has_digits("123dr"))
print(has_digits("ytfcyhc"))











