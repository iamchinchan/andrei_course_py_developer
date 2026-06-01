import re

password = "sdfsdf@113434"
pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}[0-9]$")
result = pattern.search(password)
print(result)
