###########################
#  BaekJoon 2798번
#  by 김승현                
###########################

# Q. 블랙잭

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

flag = 0
max_sum = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            _sum = num_list[i] + num_list[j] + num_list[k]
            if _sum == m:
                print(m)
                flag = 1
                break
            elif _sum < m and _sum > max_sum:
                max_sum = _sum
        if flag == 1:
            break
    if flag == 1:
        break
if flag == 0:
    print(max_sum)