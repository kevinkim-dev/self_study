def solution(dartResult):
    score = {'S': 1, 'D': 2, 'T': 3}
    answer = 0
    temp, cnt, nums = '', 1, [0]
    for i in range(len(dartResult)):

        c = dartResult[i]
        if c in score.keys():
            temp = int(temp)**score[c]
            if i == len(dartResult)-1 or dartResult[i+1] not in ('#', '*'):
                nums.append(temp)
                temp = ''
                cnt += 1
        elif c == '*':
            nums[cnt-1] *= 2
            nums.append(temp * 2)
            temp = ''
            cnt += 1
        elif c == '#':
            nums.append(-temp)
            temp = ''
            cnt += 1
        else:
            temp += c
    return sum(nums)
        # print(i, temp, nums)
print(solution('1S2D*3T'))