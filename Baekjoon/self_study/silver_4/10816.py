###########################
#  BaekJoon 10816번
#  by 김승현                
###########################

# Q. 숫자 카드 2

N = int(input())
num_list = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

num_dict = dict()
for target in targets:
    num_dict[target] = 0

for num in num_list:
    if num in num_dict.keys():
        num_dict[num] += 1

ans = []
for target in targets:
    ans.append(str(num_dict[target]))

print(' '.join(ans))