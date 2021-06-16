def solution(N):
    cnt, max_cnt, flag = 0, 0, 0
    while N:
        bit = N % 2
        N //= 2
        if bit:
            if flag:
                max_cnt = max(cnt, max_cnt)
                cnt = 0
            else:
                cnt = 0
                flag = 1
        else:
            cnt += 1
    return max_cnt