def solution(skill, skill_trees): 
    
    def check_skill(skill, sk):
        i = -1
        for s in sk:
            if s in skill and skill.index(s) != i+1:
                return False
            elif s in skill:
                i = skill.index(s)
        return True
    
    answer = 0
    for sk in skill_trees:
        answer += int(check_skill(skill, sk))
    return answer