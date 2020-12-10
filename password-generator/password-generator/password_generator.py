"strong passwords include mix of upper/lower-case letters, numbers and symbols"

import string
import random

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = ""

for i in range(1,16):
    password += random.choice(chars)

print(password)