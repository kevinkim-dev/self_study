def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    while A and B:
        a = A.pop()
        while B:
            b = B.pop()
            if b > a:
                answer += 1
                break
    if B:
        answer += len(B)
    return answer