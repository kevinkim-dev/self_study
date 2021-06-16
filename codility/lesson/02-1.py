def solution(A, K):
    l = len(A)
    if l:
        K %= l
        return A[l-K:] + A[:l-K]
    else:
        return []