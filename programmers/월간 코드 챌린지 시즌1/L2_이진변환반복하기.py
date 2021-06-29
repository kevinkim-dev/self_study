import time

def solution(s):
    cnt, zeros = 0, 0
    while s != '1':
        l1 = len(s)
        s = s.replace('0', '')
        l2 = len(s)
        s = bin(l2)[2:]
        zeros += l1 - l2
        cnt += 1
    return [cnt, zeros]

print(solution('01110'))