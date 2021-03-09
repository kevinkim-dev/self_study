#########################
#  SWEA number 1216
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

def check_palindrom(string, length, max_pal):
    if length <= max_pal:
        return 1
    for i in range(le+1-length):
        check_string = string[i:i+length]
        if palindrom(check_string):
            return length
    return check_palindrom(string, length-1, max_pal)

for i in range(10):
    t = int(input())
    le = 100
    box = [0]*le
    max_pal = 0
    for i in range(le):
        string = input()
        box[i] = string
        pal = check_palindrom(string + ' ', le, max_pal)
        if pal > max_pal:
            max_pal = pal
    for col in range(le):
        string = ''
        for row in range(le):
            string += box[row][col]
        pal = check_palindrom(string + ' ', le, max_pal)
        if pal > max_pal:
            max_pal = pal
    print("#%d %d" %(t, max_pal))