def solution(n):
    answer = [[0]*(i+1) for i in range(n)]
    i, num, r = 0, 1, -1
    while i < n:
        if i % 3 == 0:
            for j in range(1, n-i+1):
                answer[r+j][i//3] = num
                num += 1
            r += j
        elif i % 3 == 1:
            for j in range(1, n-i+1):
                answer[r][i//3+j] = num
                num += 1
        else:
            for j in range(1, n-i+1):
                answer[r-j][-i//3] = num
                num += 1
            r -= j
        i += 1
    ans = []
    for a in answer:
        ans.extend(a)
    return ans

solution(5)