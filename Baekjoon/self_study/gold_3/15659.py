###########################
#  BaekJoon 15659번
#  by 김승현                
###########################

# Q. 연산자 끼워넣기 (3)

operator = ['+', '-', '*', '//']

def cal(exp, cnt):
    if cnt == N:
        res = eval(exp)
        ans[0] = max(ans[0], res)
        ans[1] = min(ans[1], res)
        return
    for i in range(4):
        if op_num[i]:
            op_num[i] -= 1
            cal(exp + operator[i] + num_list[cnt], cnt + 1)
            op_num[i] += 1
    return

import sys

input = sys.stdin.readline

N = int(input())

num_list = input().split()

op_num = list(map(int, input().split()))

ans = [-1000000000, 1000000000]

cal(num_list[0], 1)

print(ans[0])
print(ans[1])