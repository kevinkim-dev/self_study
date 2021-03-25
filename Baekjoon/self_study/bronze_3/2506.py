###########################
#  BaekJoon 2506번
#  by 김승현                
###########################

# Q. 점수계산

N = int(input())
q_list = list(map(int, input().split()))
con = 1
score = 0
for n in range(N):
    if q_list[n] == 0:
        con = 1
    else:
        score += con
        con += 1
print(score)