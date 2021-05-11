#########################
#  Programmers problem
#  Kakao internship 2021
#  by 김승현                
#########################

# Q. 1번

def solution(s):
    s += 'x'
    answer = ''
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while s[0] != 'x':
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            if s[0:3] in nums:
                answer += str(nums.index(s[0:3]))
                s = s[3:]
            elif s[0:4] in nums:
                answer += str(nums.index(s[0:4]))
                s = s[4:]
            else:
                answer += str(nums.index(s[0:5]))
                s = s[5:]
    return answer


s = "one4seveneight"
print(solution(s))