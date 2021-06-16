###########################
#  BaekJoon 1874번
#  by 김승현                
###########################

# Q. 스택 수열

idx, flag = 1, 1
targets = []
num_stack = list()
ans = []
N = int(input())
pop_target = set()

for _ in range(N):
    targets.append(int(input()))

for target in targets:
    if idx <= target:
        push_set = set(range(idx, target)) - pop_target
        num_stack = list(set(num_stack) | push_set)
        ans += ['+']*(len(push_set) + 1) + ['-']
        idx = target
    else:
        if num_stack.pop() == target:
            ans += ['-']
        else:
            flag = 0
            break
    pop_target.add(target)

if flag:
    for a in ans:
        print(a)
else:
    print('NO')
