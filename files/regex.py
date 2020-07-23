import re

text = "huntermacias20@gmail.com"
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

a = pattern.search(text)
b = pattern.findall(text)
c = pattern.fullmatch(text) #text must the exact same as the pattern for this to return true
d = pattern.match(text) #returns a match if the two strings match at the beginning

print(a.start())
print(a.end())
print(a.group())
print(a.span())

print(b)

print(c)

print(d)