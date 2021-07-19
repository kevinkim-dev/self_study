def solution(n, t, m, timetable):
    answer = ''
    bus_table, crew_table = list(), list()
    for i in range(n):
        bus_table.append(540+t*i)
    for time in timetable:
        hh, mm = time.split(':')
        crew_table.append(int(hh)*60 + int(mm))
    crew_table.sort(reverse=True)
    for i in range(n):
        bus, cnt = bus_table[i], 0
        if i != n-1:
            while cnt < m and crew_table:
                if crew_table[-1] <= bus:
                    crew_table.pop()
                else:
                    break
            if not crew_table:
                last = bus_table[-1]
                break
        else:
            last_crews = dict()
            for i in range(len(crew_table)-1, -1, -1):
                c = crew_table[i]
                if c <= bus:
                    last_crews[c] = last_crews.get(c, 0) + 1
                else:
                    break
            if sum(last_crews.values()) < m:
                last = bus
            else:
                print('hi')
                for key in sorted(last_crews.keys()):
                    if last_crews[key] >= m:
                        last = key - 1
                        break
                    else:
                        m -= last_crews[key]
    answer = str(last//60).zfill(2) + ':' + str(last%60).zfill(2)
    return answer

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))