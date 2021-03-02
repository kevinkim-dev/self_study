###########################
#  BaekJoon 7568번
#  by 김승현                
###########################

# Q. 덩치

N = int(input())

people_list = [list(map(int, input().split())) for n in range(N)]
people_rank = [0]*N

for n in range(N):
    cnt = 0
    weight = people_list[n][0]
    height = people_list[n][1]
    for i in range(N):
        if weight < people_list[i][0] and height < people_list[i][1]:
            cnt += 1
    people_rank[n] = cnt + 1
print(*people_rank)


# # while True:
# max_w = 0
# for n in range(N):
#     if people_list[n][0] > max_w:
#         n = max_index

# print(max_w)

# print(people_list)

# for i in range(N-1, -1, -1):
#     for j in range(i):
#         if people_list[j][0] < people_list[j+1][0]:
#             people_list[j], people_list[j+1] = people_list[j+1], people_list[j]
        