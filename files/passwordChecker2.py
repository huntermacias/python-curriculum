import re


pattern = re.compile(r"[A-Za-z0-9$%&#@]{8,}\d")
password = "werjsznx$#2"

pass1 = pattern.fullmatch(password)
print(pass1)