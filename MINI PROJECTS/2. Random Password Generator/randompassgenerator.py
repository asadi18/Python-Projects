import random
import string

pass_len = 12

CharValues = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(pass_len):
#     password += random.choice(CharValues)
    
# print(password)


#list  Comprehension Technique for this [function i in range()]

password = "".join([random.choice(CharValues) for i in range(pass_len)])
print(password)