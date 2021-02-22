###########################
#  BaekJoon 11549번
#  by 김승현                
###########################

# Q. Identifying tea

n = int(input())
answer_list = list(map(int, input().split()))
cnt = 0
for tea in answer_list:
    if tea == n:
        cnt += 1
print(cnt)