def solution(n):
    bits = list()
    while n:
        bits.append(n % 3)
        n //= 3
    answer = 0
    for i in range(len(bits)):
        answer += bits[-i-1]*3**(i)
    return answer
