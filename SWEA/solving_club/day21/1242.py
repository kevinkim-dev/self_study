
#########################
#  SWEA number 1242
#  by 김승현                
#########################

# Q. 암호코드 스캔

# import sys
# sys.stdin = open("input.txt", "r")

# def find_digit(x):
#     bit = 0
#     cnt, total_cnt = 0, []
#     for b in x:
#         if b == str(bit):
#             cnt += 1
#         else:
#             bit = int(not bit)
#             total_cnt.append(cnt)
#             cnt = 1
#     total_cnt.append(cnt)
#     # print(total_cnt)
#     if len(total_cnt) != 4:
#         return -1
#     min_cnt = min(total_cnt)
#     max_gcd = 0
#     for n in range(1, min_cnt+1):
#         for c in total_cnt:
#             if c % n != 0:
#                 break
#             max_gcd = n
#     for i in range(4):
#         total_cnt[i] //= max_gcd
#     # print(total_cnt)
#     if total_cnt in code:
#         return code.index(total_cnt)
#     else:
#         return -1


# def check_password(x):
#     return ((x[0]+x[2]+x[4]+x[6])*3+x[1]+x[3]+x[5]+x[7]) % 10 == 0

# code = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

# for t in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     ans = 0
#     passwords = []
#     for _ in range(N):
#         line = bin(int(input(), 16))[2:].zfill(M*4)
#         while line.count('0') != len(line):
#             line = line.rstrip('0')
#             # print(line)
#             mul = 1
#             while True:
#                 # print(mul)
#                 password_slice = line[-7 * mul:]
#                 mul += 1
#                 if password_slice[0] == '1':
#                     continue
#                 # print(password_slice)
#                 found_num = find_digit(password_slice)
#                 if found_num != -1:
#                     break
#             mul -= 1
#             correct_password_slice = line[-56 * mul:]
#             # print(correct_password_slice)
#             line = line[:-56*mul]
#             password = []
#             for i in range(8):
#                 # print(correct_password_slice[i*7*mul:(i+1)*7*mul])
#                 password.append(find_digit(correct_password_slice[i*7*mul:(i+1)*7*mul]))
#             if check_password(password) and password not in passwords:
#                 ans += sum(password)
#                 passwords.append(password)
#     print("#%d %d" %(t, ans))
        
def find_digit(x):
    bit = 0
    cnt, total_cnt = 0, []
    for b in x:
        if b == str(bit):
            cnt += 1
        else:
            bit = int(not bit)
            total_cnt.append(cnt)
            cnt = 1
    total_cnt.append(cnt)
    if len(total_cnt) != 4:
        return -1
    min_cnt = min(total_cnt)
    max_gcd = 0
    for n in range(1, min_cnt+1):
        for c in total_cnt:
            if c % n != 0:
                break
            max_gcd = n
    for i in range(4):
        total_cnt[i] //= max_gcd
    if total_cnt in code:
        return code.index(total_cnt)
    else:
        return -1


def check_password(x):
    return ((x[0]+x[2]+x[4]+x[6])*3+x[1]+x[3]+x[5]+x[7]) % 10 == 0

code = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = 0
    passwords = []
    for _ in range(N):
        line = bin(int(input(), 16))[2:].zfill(M*4)
        while line.count('0') != len(line):
            line = line.rstrip('0')
            mul = 1
            while True:
                password_slice = line[-7 * mul:]
                mul += 1
                if password_slice[0] == '1':
                    continue
                found_num = find_digit(password_slice)
                if found_num != -1:
                    break
            mul -= 1
            correct_password_slice = line[-56 * mul:]
            line = line[:-56*mul]
            password = []
            for i in range(8):
                password.append(find_digit(correct_password_slice[i*7*mul:(i+1)*7*mul]))
            if check_password(password) and password not in passwords:
                ans += sum(password)
                passwords.append(password)
    print("#%d %d" %(t, ans))
                



# def check_password(x):
#     return ((x[0]+x[2]+x[4]+x[6])*3+x[1]+x[3]+x[5]+x[7]) % 10 == 0

# code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

# for t in range(1, int(input())+1):
#     a, b = map(int, input().split())
#     rows = []
#     password = []
#     flag = 1
#     for _ in range(a):
#         row = input()
#         if '1' in row:
#             rows.append(row.rstrip('0'))
#             if rows[-1] != rows[0]:
#                 flag = 0
#     if flag:
#         row = rows[0][-56:]
#         for n in range(8):
#             letter = row[n*7:n*7+7]
#             if letter not in code:
#                 flag = 0
#                 break
#             else:
#                 password.append(code.index(letter))
#     if check_password(password) and flag:
#         print("#%d %d" %(t, sum(password)))
#     else:
#         print("#%d 0" %t)
        