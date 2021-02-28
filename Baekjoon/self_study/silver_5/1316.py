###########################
#  BaekJoon 1316번
#  by 김승현                
###########################

# Q. 그룹 단어 체커

n = int(input())
not_group = 0
for t in range(n):
    string = input()
    char_list = []
    now_char = ''
    for char in string:
        if now_char != char and char in char_list:
            not_group += 1
            break
        elif now_char == char:
            pass
        else:
            now_char = char
            char_list.append(char)

print(n-not_group)