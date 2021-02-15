###########################
#  BaekJoon 5596번
#  by 김승현                
###########################

# Q. 시험 점수

MG = list(map(int, input().split()))
MS = list(map(int, input().split()))

MG_sum = 0
MS_sum = 0
for i in range(4):
    MG_sum += MG[i]
    MS_sum += MS[i]

if MG_sum >= MS_sum:
    print(MG_sum)
else:
    print(MS_sum)