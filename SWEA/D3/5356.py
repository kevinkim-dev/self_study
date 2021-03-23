#########################
#  SWEA number 5356
#  by 김승현                
#########################

# Q. 의석이의 세로로 말해요

for t in range(1, int(input())+1):
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
    print("#%d %s" %(t,string))
    