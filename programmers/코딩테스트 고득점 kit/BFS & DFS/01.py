#########################
#  Programmers problem kit 
#  BFS & DFS # 01
#  by 김승현                
#########################

# Q. 타겟 넘버

def solution(numbers, target):
    answer = 0
    l = len(numbers)
    ans_list = [(numbers[0], 1), (-numbers[0], 1)]
    while ans_list:
        sm, idx = ans_list.pop()
        if idx == l:
            if sm == target:
                answer += 1
            continue
        ans_list.append((sm + numbers[idx], idx + 1))
        ans_list.append((sm - numbers[idx], idx + 1))
    return answer