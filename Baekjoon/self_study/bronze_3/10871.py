###########################
#  BaekJoon 10871번
#  by 김승현                
###########################

# Q. X보다 작은 수

n, x = map(int, input().split())
num_list = list(map(int, input().split()))
ans = []
for num in num_list:
    if num < x:
        ans += [num]
print(*ans)