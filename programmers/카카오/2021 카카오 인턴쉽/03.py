#########################
#  Programmers problem
#  Kakao internship 2021
#  by 김승현                
#########################

# Q. 3번

def solution(n, k, cmd):
    answer = ''
    data, data_fix = list(range(n)), list(range(n))
    deleted_data = []
    for c in cmd:
        if c == 'C':
            deleted_data.append(data[k])
            data = data[:k] + data[k+1:]
            if k >= len(data):
                k -= 1
        elif c == 'Z':
            ctrlz = deleted_data.pop()
            if ctrlz < data[k]:
                k += 1
            data.append(ctrlz)
            data.sort()
        elif c[0] == 'U':
            k -= int(c[2:])
        else:
            k += int(c[2:])
    for d in data_fix:
        if d in data:
            answer += 'O'
        else:
            answer += 'X'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))


# from collections import deque

# def solution(n, k, cmd):
#     answer = ''
#     data, data_fix = deque(range(n)), deque(range(n))
#     deleted_data = deque()
#     for c in cmd:
#         if c == 'C':
#             data.rotate(-k)
#             deleted_data.append(data.popleft())
#             data.rotate(k)
#             if k >= len(data):
#                 k -= 1
#         elif c == 'Z':
#             ctrlz = deleted_data.pop()
#             if ctrlz < data[k]:
#                 k += 1
#             data.append(ctrlz)
#             # data.sort()
#         elif c[0] == 'U':
#             k -= int(c[2:])
#         else:
#             k += int(c[2:])
#     for d in data_fix:
#         if d in data:
#             answer += 'O'
#         else:
#             answer += 'X'
#     return answer