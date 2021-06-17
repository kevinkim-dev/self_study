def solution(A):
    a, b = A[0], sum(A) - A[0]
    min_dif = abs(a-b)
    for i in range(1, len(A)-1):
        num = A[i]
        a += num
        b -= num
        min_dif = min(min_dif, abs(a-b))
    return min_dif