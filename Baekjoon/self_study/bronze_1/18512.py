###########################
#  BaekJoon 18512번
#  by 김승현                
###########################

# Q. 점프 점프

def gcd(num1, num2):
    while max(num1, num2) % min(num1, num2):
        num1, num2 = max(num1, num2) - min(num1, num2), min(num1, num2)
    return min(num1, num2)

import sys

input = sys.stdin.readline

x, y, p1, p2 = map(int, input().split())

loop = x*y//gcd(x, y)

if p1 > p2:
    p1, p2 = p2, p1
    x, y = y, x

ans = -1
for i in range(loop//y):
    if (p2 - p1 + y * i) % x:
        continue
    ans = y*i + p2
    break

print(ans)