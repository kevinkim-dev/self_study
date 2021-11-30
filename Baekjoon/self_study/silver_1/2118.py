###########################
#  BaekJoon 2118번
#  by 김승현                
###########################

# Q. 두 개의 탑

N = int(input())

num_list = []

for _ in range(N):
    num_list.append(int(input()))

total = sum(num_list)

max_dist = 0

for i in range(N):
    dist = 0
    for j in range(i, N):
        dist += num_list[j]
        max_dist = max(max_dist, min(dist, total-dist))
        if dist > total - dist:
            break

print(max_dist)
        
