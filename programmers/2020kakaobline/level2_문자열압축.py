###########################
#  Kakao blind 2020 
#  Level2_문자열압축
#  by 김승현                
###########################

def solution(s):
    l, answer = len(s), len(s)
    for i in range(1, l//2+1):
        temp = 0
        cut = s[:i]
        cut_list = [[cut, 1]]
        for j in range(1, l//i):
            if s[j*i:(j+1)*i] == cut:
                cut_list[-1][1] += 1
            else:
                cut = s[j*i:(j+1)*i]
                cut_list.append([cut, 1])
        if l%i != 0:
            cut_list.append([s[i*(l//i):], 1])
        for a, b in cut_list:
            temp += len(a)
            if b != 1:
                temp += len(str(b))
        answer = min(answer, temp)
    return answer

s = 'aabbaccc'
print(solution(s))