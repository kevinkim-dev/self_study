###########################
#  BaekJoon 2566번
#  by 김승현                
###########################

# Q. 최댓값 

ans = 0
x, y = 0, 0
for i in range(9):
    num_list = list(map(int, input().split()))
    for j in range(9):
        if num_list[j] > ans:
            ans = num_list[j]
            x = i + 1
            y = j + 1

print(ans)
print(x, y)