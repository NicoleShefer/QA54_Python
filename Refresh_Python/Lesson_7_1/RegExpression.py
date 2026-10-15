import re

text = "The status is passed"
result = re.search("passed",text)
print(result)
print(result.group())

text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("passed",text2))
print(re.match("passed",text3))

print(re.search("d.g","dog"))
print(re.search("d.g","dig"))
print(re.search("d.g","dg"))
print(re.search("d..g","doog"))

order = "ORD-12345"
assert re.fullmatch(r"ORD-\d{5}",order)

print(re.search("^Test" , "Test is start"))
print(re.search("^Test" , "Start is Test"))

print(re.search("^Test$","Start is Test"))
print(re.search("^Test$","Test is Start"))

print()

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","green"))

print()

print(re.search("[a-z]","Nicole"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","nicole"))
print(re.search("[A-Za-z]","nicole"))

print()

print(re.search("[^0-9]","123456789a"))
print(re.search("[^0-9]","123456789"))
print(re.search("[^0-9]","123.45.6"))

print(re.search('\\d',"Order #34"))
print(re.search('\\w',"Nicole!!!"))
print(re.search('\\s',"Nicole QA54"))

print(re.search(r"ab*c" , "ac" ))
print(re.search(r"ab*c" , "abc" ))
print(re.search(r"ab*c" , "abccccccc" ))

print(re.search(r"colou?r" , "color" ))
print(re.search(r"colou?r" , "colour" ))
print(re.search(r"colou?r" , "colouur" ))

print(re.search(r"\d{4}" , "13" ))
print(re.search(r"\d{4}" , "1566663" ))
print(re.search(r"\d{2,4}" , "123456" ))
print(re.search(r"\d{3,4}" , "323" ))





