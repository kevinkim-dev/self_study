# def solution(a):
#     answer = 0
#     num_dict = dict()
#     for n in a:
#         if not num_dict.get(n):
#             num_dict[n] = 1
#         else:
#             num_dict[n] += 1
#     items = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
#     idx = 0
#     while idx < len(items) and answer < 2*items[idx][1]:
#         num = items[idx][0]
#         cnt = 0
#         waiting = False
#         for n in a:
#             is_num = bool(n == num)
#             if not waiting:
#                 waiting_num = bool(n != num)
#                 waiting = True
#             else:
#                 if is_num == waiting_num:
#                     cnt += 2
#                     waiting = False            
#         if cnt > answer:
#             answer = cnt
#         idx += 1
#     return answer

def solution(a):
    count = dict()
    for num in a:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    max_num = 0 # 최대값 숫자
    temp_max = 0 # 임시로 저장하는 최댓값
    while max_num != -1:
        max_val = 0 # 최댓값 숫자의 갯수
        max_num = -1 # 최댓값 숫자
        second_val = 0 # 두 번째로 빈도가 높은 값
        visited = [0] * len(a)
        for num in count.items():
            if num[1] >= max_val:
                second_val = max_val
                max_val = num[1]
                max_num = num[0]
        
        cnt = 0
        # 인덱스에 따라 같은 숫자인지 판단
        for i in range(len(a)):
            if a[i] == max_num and i - 1 >= 0 and a[i - 1] != max_num and visited[i - 1] == 0:
                visited[i - 1] = 1
                cnt += 1
            elif a[i] == max_num and i + 1 < len(a) and a[i + 1] != max_num and visited[i + 1] == 0:
                visited[i + 1] = 1
                cnt += 1
            else:
                continue
        # 두 번째로 많이 나오는 빈도보다 크거나 같다면
        if cnt >= second_val:
            return cnt * 2
        else:
            if cnt * 2 > temp_max:
                temp_max = cnt * 2
            count[max_num] = -1
        
    return temp_max


a = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]
print(solution(a))