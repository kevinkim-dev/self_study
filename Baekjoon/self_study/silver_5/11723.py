###########################
#  BaekJoon 11723번
#  by 김승현                
###########################

# Q. 집합

import sys

nums = 0

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        nums = nums | (1 << (int(command[1])-1))
    elif command[0] == 'remove':
        nums = nums & ~(1 << (int(command[1])-1))
    elif command[0] == 'check':
        print(int(bool(nums & (1 << (int(command[1])-1)))))
    elif command[0] == 'toggle':
        nums = nums ^ (1 << (int(command[1])-1))
    elif command[0] == 'all':
        nums = (1 << 20) -1
    else:
        nums = 0