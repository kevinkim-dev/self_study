###########################
#  BaekJoon 10039번
#  by 김승현                
###########################

# Q. 평균 점수

_sum = 0

for i in range(5):
    score = int(input())
    if score >= 40:
        _sum += score
    else:
        _sum += 40

print(int(_sum/5))