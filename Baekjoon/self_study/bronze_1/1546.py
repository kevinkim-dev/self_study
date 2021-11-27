###########################
#  BaekJoon 1546번
#  by 김승현                
###########################

# Q. 평균

len = int(input())
score_list = list(map(int, input().split()))

max_score = 0
for n in range(len):
    if score_list[n] > max_score:
        max_score = score_list[n]

_sum = 0
for i in range(len):
    score_list[i] = (score_list[i]/max_score) * 100
    _sum += score_list[i]

print(_sum/len)
