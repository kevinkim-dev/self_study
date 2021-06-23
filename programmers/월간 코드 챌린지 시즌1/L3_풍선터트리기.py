# 시간초과
def solution(a):
    ans = 0
    for i in range(1, len(a)-1):
        if a[i] < min(a[:i]) or a[i] < min(a[i+1:]):
            ans += 1
    return ans+2

# 첫번째 풀이
def solution(a):
    ans = 0
    l = len(a)
    mins = list([a[i], a[i]] for i in range(l))
    for i in range(1, l):
        mins[i][0] = min(mins[i-1][0], a[i])
        mins[l-i-1][1] = min(mins[l-i][1], a[l-i-1])
    for i in range(l):
        if a[i] in mins[i]:
            ans += 1
    return ans

# 두번째 풀이(더 빠름)
def solution(a):
    ans = 0
    answer = set()
    l = len(a)
    m_l, m_r = float('inf'), float('inf')
    for i in range(l):
        m_l = min(m_l, a[i])
        if m_l == a[i]:
            answer.add(a[i])
        m_r = min(m_r, a[l-i-1])
        if m_r == a[l-i-1]:
            answer.add(a[l-i-1])
    return len(answer)   