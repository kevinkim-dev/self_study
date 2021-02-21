###########################
#  BaekJoon 15552번
#  by 김승현                
###########################

# Q. 빠른 A+B

import sys

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)