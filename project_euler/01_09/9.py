###########################
#  project_euler number 9
#  by 김승현                
###########################

# Q. a + b + c = 1000 이 되는 피타고라스 수

# 합에 1000이 되는 모든 a,b,c 셋 중에서
# 피타고라스 정리를 만족하는 set을 찾아본다
def DIY_find_pitNumSet(sum_pit):
    for c in range(sum_pit, 0, -1):
        for b in range(sum_pit - c-1, (sum_pit - c) // 2, -1):
            a = sum_pit - b - c
            if a*a + b*b == c*c:
                return a*b*c

print(DIY_find_pitNumSet(1000))
            

