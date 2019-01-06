import  string
from random import *
charaters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(charaters) for x in range(randint(9,16)))
print(password)