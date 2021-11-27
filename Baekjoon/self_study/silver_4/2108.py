###########################
#  BaekJoon 2108번
#  by 김승현                
###########################

# Q. 통계학

num_list = []
for _ in range(int(input())):
    num_list.append(int(input()))


num_list.sort()

max_num, max_num_cnt = [], 0

for num in set(num_list):
    cnt =  num_list.count(num)
    if cnt == max_num_cnt:
        max_num.append(num)
    elif cnt > max_num_cnt:
        max_num_cnt = cnt
        max_num = [num]

if len(max_num) == 1:
    max_num = max_num[0]
else:
    max_num = sorted(max_num)[1]


print(round(sum(num_list)//len(num_list)))
print(num_list[len(num_list)//2])
print(max_num)
print(num_list[-1]-num_list[0])  