#########################
#  SWEA number 11556
#  by 김승현                
#########################

# Q. 부분집합의 합

set_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for t in range(1, int(input())+1):
    cnt = 0
    n, _sum = map(int, input().split())
    subset_list = []
    for i in range(1<<12):
        subset = []
        for j in range(13):
            if i & (1<<j):
                subset.append(set_a[j])
        if len(subset) == n and sum(subset) == _sum:
            cnt += 1
    print("#%d %d" %(t, cnt))
