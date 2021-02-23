#########################
#  SWEA number 11579
#  by 김승현                
#########################

# Q. 반복문자 지우기

def check_con(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return i
    return -1

for t in range(1, int(input())+1):
    string = input()
    check = check_con(string)
    while check != -1:
        string = string[:check] + string[check+2:]
        check = check_con(string)
    print("#%d %d" %(t, len(string)))