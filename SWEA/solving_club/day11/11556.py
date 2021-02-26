#########################
#  SWEA number 11556
#  by 김승현  
#########################

# Q. 부분집합의 합

# 원소를 넣고 len -= 1
# 원소를 안넣고 n += 1

def subset(i):
    if i == max_num:
        cnt, _sum = 0, 0
        for idx in range(max_num):
            if arr[idx]:
                cnt += 1
                _sum += idx+1
        if cnt == n and _sum == k:
            subset_list.append(arr)
        return
    arr[i] = 1
    subset(i+1)
    arr[i] = 0
    subset(i+1)

max_num = 12

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [0]*12
    subset_list = []

    subset(0)
    print("#%d %d" %(t, len(subset_list)))