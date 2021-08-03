import math

def solution(n, stations, w):
    answer, wifi = 0, 1
    for station in stations:
        answer += math.ceil((station - w - wifi) / (2*w + 1))
        wifi = station + w + 1
    if wifi <= n:
        answer += math.ceil((n + 1 - wifi) / (2*w + 1))        
    return answer