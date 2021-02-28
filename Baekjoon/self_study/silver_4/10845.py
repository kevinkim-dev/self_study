###########################
#  BaekJoon 10845번
#  by 김승현                
###########################

# Q. 큐

import sys

n = int(sys.stdin.readline().strip())
stack = []
for _ in range(n):
    string = sys.stdin.readline().strip()
    if string == 'back':
        print(stack[-1]) if stack else print('-1')
    elif string == 'front':
        print(stack[0]) if stack else print('-1')
    elif string == 'size':
        print(len(stack))
    elif string == 'pop':
        print(stack.pop(0)) if stack else print('-1')
    elif string == 'empty':
        print(int(not bool(stack)))
    else:
        string = string.split()
        stack.append(string[1])