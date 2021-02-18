#########################
#  SWEA number 11561
#  by 김승현                
#########################

# Q. 문자열 뒤집기

for t in range(1, int(input())+1):
    string = input()
    new_string = ''
    for i in range(len(string)-1, -1, -1):
        if string[i] == ' ' and new_string == '':
            continue
        new_string += string[i]
    print("#%d %s" %(t, new_string))
    