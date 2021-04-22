#########################
#  Programmers problem kit 
#  정렬 # 01
#  by 김승현                
#########################

# Q. K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer