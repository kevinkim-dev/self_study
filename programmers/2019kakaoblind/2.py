def solution(record):
    answer = []
    record_split, record_change = [], []
    id_set = set()
    
    for i in range(len(record)):
        rec = list(record[i].split())
        record_split.append(rec)
        id_set.add(rec[1])
    id_done = dict()

    while record_split:
        data = record_split.pop()
        if data[1] not in id_done.keys() and len(data) == 3:
            id_done[data[1]] = data[2]
        record_change.append(data)

    while record_change:
        rec = record_change.pop()
        if rec[0] == 'Enter':
            answer.append(id_done[rec[1]] + '님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            answer.append(id_done[rec[1]] + '님이 나갔습니다.')
    return answer