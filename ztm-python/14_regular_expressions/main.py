import re
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/
# https://regexone.com/
# https://emailregex.com/

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'search this inside of this text please! Whom text...'
string = 'neena@dog.com'
# print('search' in string)
# print(re.search('this', string))
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string) # must match entirely
d = pattern.match(string)

print(a)


# make a pw 8+ chars long, start with letter
# letters, numbers, $%#@
pwpattern = re.compile(r"(^[a-zA-Z][a-zA-Z0-9$%#@]{7,}$)")
userpw = 'superezpassword'
a = pwpattern.search(userpw)
print(a)
