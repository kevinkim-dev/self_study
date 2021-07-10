def solution(n, arr1, arr2):
    answer = []
    key = [' ', '#']
    for _ in range(n):
        ans = ''
        a, b = arr1.pop(0), arr2.pop(0)
        bi = a | b
        for _ in range(n):
            ans = key[bi % 2] + ans 
            bi //= 2
        answer.append(ans)
    return answer