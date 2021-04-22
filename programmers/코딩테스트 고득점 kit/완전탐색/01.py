#########################
#  Programmers problem kit 
#  완전탐색 # 01
#  by 김승현                
#########################

# Q. 모의고사

def solution(answers):
    p_list = [0, 0, 0]
    b_list = [1, 3, 4, 5]
    c_list = [3, 1, 2, 4, 5]
    for i in range(len(answers)):
        if answers[i] % 5 == i % 5 + 1:
            p_list[0] += 1
        if (not i % 2 and answers[i] == 2) or (i % 2 and b_list[(i-1)//2 % 4] == answers[i]):
            p_list[1] += 1
        if c_list[(i % 10) // 2] == answers[i]:
            p_list[2] += 1
    answer = []
    max_answer = 0
    for idx in range(3):
        if p_list[idx] > max_answer:
            max_answer = p_list[idx]
            answer = [idx + 1]
        elif p_list[idx] == max_answer:
            answer.append(idx+1)
    if not answer:
        answer = [1, 2, 3]
    return answer

answer = [1, 3, 2, 4, 2]
print(solution(answer))