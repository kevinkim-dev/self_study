###########################
#  BaekJoon 10798번
#  by 김승현                
###########################

# Q. 세로읽기

str_list = [0]*5
max_length = 0
for i in range(5):
    str_list[i] = input()
    if len(str_list[i]) > max_length:
        max_length = len(str_list[i])
string = ''
for l in range(max_length):
    for i in range(5):
        try:
            string += str_list[i][l]
        except IndexError:
            continue
print(string)