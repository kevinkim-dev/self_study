#########################
#  Programmers problem kit 
#  summer 05월
#  by 김승현                
#########################

# Q. 1번

def solution(left, right):  
    answer = 0
    for num in range(left, right+1):
        if num ** 0.5 - int(num ** 0.5) < 1e-9:
            answer -= num
        else:
            answer += num
    return answer

left = 13
right = 17
print(solution(left, right))