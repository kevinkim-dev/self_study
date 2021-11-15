###########################
#  BaekJoon 10820번
#  by 김승현                
###########################

# Q. 문자열 분석

while True:
    try:
        string = input()
        array = [0, 0, 0, 0]
        for s in string:
            if s.isnumeric():
                array[2] += 1
            elif s == ' ':
                array[3] += 1
            elif s.isupper():
                array[1] += 1
            else:
                array[0] += 1
        print(' '.join(list(map(str, array))))
    except EOFError:
        break
