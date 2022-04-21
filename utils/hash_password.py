import re


def hash_password(password):
    preFix = "#90091"
    add_preFix = True

    if re.search(rf"^{preFix}", password):
        password = re.sub(rf"^{preFix}", "", password)
        add_preFix = False

    abc = "ulOXntwCgdiNkMfvhbLKxzWErVFHcDjSyTJPaeUZqosBAIRmpYQG"
    ABC = "KwCWaVlOhTFEHpvfgSeuDcXNqtikzxAbIdGYnLZUrBQojymRMPsJ"
    numbers = "2016574398"
    NUMBERS = "3650198274"
    symbols = "@_!~^|%#-+*=&$"
    SYMBOLS = "^~-_@%|*!$#&=+"

    hashed_password = ""

    for n in password:
        if n in abc:
            for num in range(len(abc)):
                if n == abc[num]:
                    n = ABC[num]
                    hashed_password += n
                    break
        elif n in numbers:
            for num in range(len(numbers)):
                if n == numbers[num]:
                        n = NUMBERS[num]
                        hashed_password += n
                        break
        elif n in symbols:
            for num in range(len(symbols)):
                if n == symbols[num]:
                        n = SYMBOLS[num]
                        hashed_password += n
                        break
        else:
            hashed_password += n
    
    if add_preFix:
        return preFix + hashed_password
    return hashed_password

# password1 = "hello world !!"
# password2 = hash_password(password1)

# print(password1)
# print(password2)
# print(hash_password(password2))
# print(password1 == hash_password(password2))
