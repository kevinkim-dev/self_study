#########################
#  SWEA number 1240
#  by 김승현                
#########################

# Q. 단순 2진 암호코드

def check_password(x):
    return ((x[0]+x[2]+x[4]+x[6])*3+x[1]+x[3]+x[5]+x[7]) % 10 == 0

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    rows = []
    password = []
    flag = 1
    for _ in range(a):
        row = input()
        if '1' in row:
            rows.append(row.rstrip('0'))
            if rows[-1] != rows[0]:
                flag = 0
    if flag:
        row = rows[0][-56:]
        for n in range(8):
            letter = row[n*7:n*7+7]
            if letter not in code:
                flag = 0
                break
            else:
                password.append(code.index(letter))
    if check_password(password) and flag:
        print("#%d %d" %(t, sum(password)))
    else:
        print("#%d 0" %t)

        