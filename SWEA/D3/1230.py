#########################
#  SWEA number 1230
#  by 김승현                
#########################

# Q. 암호문3

import sys

sys.stdin = open("input.txt")

for t in range(1, 11):
    length = int(input())
    password = input().split()
    work_num = int(input())
    works = input().split()
    for i in range(len(works)):
        if works[i] == 'I':
            password = password[:int(works[i+1])] + works[i+3:i+3+int(works[i+2])] + password[int(works[i+1]):]
        elif works[i] == 'D':
            password = password[:int(works[i+1])] + password[int(works[i+1])+int(works[i+2]):]
        elif works[i] == 'A':
            password.extend(works[i+2:i+2+int(works[i+1])])
    print("#%d" %t, end=' ')
    print(*password[:10])

# for t in range(1, 11):
#     length = int(input())
#     password = input().split()
#     work_num = int(input())
#     works = input().split()
#     for i in range(work_num):
#         if works[i] == 'I':
#             password = password[:int(works[i+1])] + works[i+3:i+3+int(works[i+2])] + password[int(works[i+1]):]
#         elif works[i] == 'D':
#             password = password[:int(works[i+1])] + password[int(works[i+1])+int(works[i+2]):]
#         elif works[i] == 'A':
#             password.extend(works[i+2:i+2+int(works[i+1])])
#     print(*password[:10])

# for t in range(1, 11):
#     length = int(input())
#     password = input().split()
#     work_num = int(input())
#     works = input().split()
#     work_count = 0
#     i = 0
#     while work_count == work_num:
#         if works[i] == 'I':
#             password = password[:int(works[i+1])] + works[i+3:i+3+int(works[i+2])] + password[int(works[i+1]):]
#             i += 3 + works[i+2]
#         elif works[i] == 'D':
#             password = password[:int(works[i+1])] + password[int(works[i+1])+int(works[i+2]):]
#             i += 3
#         elif works[i] == 'A':
#             password.extend(works[i+2:i+2+int(works[i+1])])
#             i += 2 + works[i+2]
#         work_count += 1
#     print(*password[:10])