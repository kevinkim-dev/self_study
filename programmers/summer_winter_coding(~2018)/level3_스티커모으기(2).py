def solution(sticker):
    answer = 0
    l = len(sticker)
    if l == 1:
        answer = sticker[0]
    else:
        s1_sum, s2_sum, s3_sum = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        for i in range(l-1):
            s1_sum.append(max(s1_sum[-1], s1_sum[-2] + sticker[i], s1_sum[-3] + sticker[i]))
            s2_sum.append(max(s2_sum[-1], s2_sum[-2] + sticker[i-1], s2_sum[-3] + sticker[i-1]))
            s3_sum.append(max(s3_sum[-1], s3_sum[-2] + sticker[i-2], s3_sum[-3] + sticker[i-2]))
        answer = max(s1_sum[-1], s2_sum[-1], s3_sum[-1])
    
    return answer