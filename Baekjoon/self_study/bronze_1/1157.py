###########################
#  BaekJoon 1157번
#  by 김승현                
###########################

# Q. 단어공부

alpha_list = [0]*26

string = input()

for i in range(len(string)):
    char = string[i]
    if ord(char) >= 65 and ord(char) <= 90:
        alpha_list[ord(char)-65] += 1
    elif ord(char) >= 97 and ord(char) <= 122:
        alpha_list[ord(char)-97] += 1

max_count = 0
max_count_index = 0
same_flag = 0
for i in range(26):
    if alpha_list[i] > max_count:
        max_count = alpha_list[i]
        max_count_index = i
        same_flag = 0
    elif alpha_list[i] == max_count:
        same_flag = 1

if same_flag == 0:
    print(chr(max_count_index + 65))
else:
    print("?")
