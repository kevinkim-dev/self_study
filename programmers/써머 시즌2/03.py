#########################
#  Programmers problem kit 
#  summer 05월
#  by 김승현                
#########################

# Q. 3번

def solution(s):
    answer = []
    for num in s:
        temp_num = ''
        idx = 0
        while '110' in num[idx:] and '111' in num[idx:]:
            a, b = num.index('110'), num.index('111')
            if a < b:
                temp_num += num[:a] + num[a+3:b] + '110'
                num = num[b:]
                continue
            temp_num += num[:b] + '110'
            num = num[b:a] + num[a+3:]
        split_a = num.split('110')
        l_110 = len(split_a)-1
        num = ''.join(split_a)
        if not num:
            num = '110'*l_110
        elif len(num) == 1:
            if num[-1] == '1':
                num = num[:-1] + '110'*l_110 + '1'
            else:
                num += '110'*l_110
        else:
            if num[-1] == '1' and num[-2] == '1':
                num = num[:-2] + '110'*l_110 + '11'
            else:
                num += '110'*l_110
        temp_num += num
        answer.append(temp_num)
    return answer

s = ["1110","100111100","0111111010"]
print(solution(s))