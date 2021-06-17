###########################
#  BaekJoon 1874번
#  by 김승현                
###########################

# Q. 스택 수열

idx, flag = 0, 1
targets = []
num_stack = list()
ans = []
N = int(input())

for _ in range(N):
    targets.append(int(input()))

for target in targets:
    if idx <= target:
        push_list = list(range(idx + 1, target))
        num_stack += push_list
        ans += ['+']*(len(push_list)+1) + ['-']
        idx = target
    else:
        if num_stack.pop() == target:
            ans += ['-']
        else:
            flag = 0
            break

if flag:
    for a in ans:
        print(a)
else:
    print('NO')
