def solution(lines):
    timeline = []
    for line in lines:
        data = line.split()[1:3]
        time = data[0].split(':')
        print(time)
        if '.' in data[1][:-1]:
            sec, m_sec = data[1][:-1].split('.')
        else:
            sec, m_sec = data[1][0], '0'
        runtime = int(sec)*1000 + int(m_sec + '0'*(3 - len(m_sec)))
        
    answer = 0
    return answer


def solution(lines):
    timeline = []
    for line in lines:
        data = line.split()[1:3]
        time = data[0].split(':')
        time = int(time[0])*60*60 + int(time[1])*60 + float(time[2])
        print(time)
        runtime = float(data[1][:-1])
        print(runtime)
        timeline.append((time, 1))
        timeline.append((time-runtime + 0.001, 0))
    print(timeline)
    answer = 0
    return answer