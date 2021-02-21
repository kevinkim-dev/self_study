###########################
#  BaekJoon 11655번
#  by 김승현                
###########################

# Q. ROT13

string = input()
new_string = ''

for char in string:
    if ord(char) >= 65 and ord(char) <= 77:
        new_string += chr(ord(char)+13)
    elif ord(char) >= 78 and ord(char) <= 90:
        new_string += chr(ord(char)-13)
    elif ord(char) >= 97 and ord(char) <= 109:
        new_string += chr(ord(char)+13)
    elif ord(char) >= 110 and ord(char) <= 122:
        new_string += chr(ord(char)-13)
    else:
        new_string += char
print(new_string)