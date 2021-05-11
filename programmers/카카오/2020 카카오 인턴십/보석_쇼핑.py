#########################
#  Programmers problem
#  Kakao internship 2020
#  by 김승현                
#########################

# Q. 보석 쇼핑

def solution(gems):
    answer = [1, len(gems)]
    gem_count = len(set(gems))
    s = 0
    min_len = len(gems)
    if gem_count == 1:
        answer = [1, 1]
    else:
        for e in range(1, len(gems)):
            while gems[s:e+1].count(gems[s]) > 1:
                s += 1
            if len(set(gems[s:e+1])) == gem_count and e-s+1 < min_len:
                min_len = e-s+1
                answer = [s+1, e+1]
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))