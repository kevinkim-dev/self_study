#########################
#  SWEA number 1215
#  by 김승현                
#########################

# Q. 회문

def palindrom(pal):
    string = pal
    while string:
        if string[0] == string[-1]:
            string = string[1:-1]
        else:
            return False
    return True

def check_palindrom(string, length):
    pal_cnt = 0
    for i in range(len(string)-length+1):
        if palindrom(string[i:i+length]):
            pal_cnt += 1
    return pal_cnt


for t in range(1, 11):
    length = int(input())
    le = 8
    box = [0]*le
    cnt = 0
    for i in range(le):
        string = input()
        box[i] = string
        cnt += check_palindrom(string, length)
    for col in range(le):
        string = ''
        for row in range(le):
            string += box[row][col]
        cnt += check_palindrom(string, length)
    print("#%d %d" %(t, cnt))