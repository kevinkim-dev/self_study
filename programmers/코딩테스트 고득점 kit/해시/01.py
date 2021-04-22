#########################
#  Programmers problem kit 
#  해쉬 # 01
#  by 김승현                
#########################

# Q. 완주하지 못한 선수

def solution(participant, completion):
    for p in completion:
        if p in participant:
            participant.remove(p)
    answer = participant[0]
    return answer