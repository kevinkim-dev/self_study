# for _ in range(int(input())):
#     N = int(input())
#     data = [0] + list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     result = 0
#     for i in range(1, N + 1):
#         # 이미 싸이클에 포함된 학생
#         if visited[i]:
#             continue
            
#         idx = i
#         cnt = 0
#         cycle_dict = {idx: cnt}
#         cycle = {idx}
#         while True:
#             visited[idx] = 1
#             cycle.add(idx)
#             cycle_dict[idx] = cnt
#             if data[idx] in cycle:
#                 result += cycle_dict[data[idx]]
#                 break

#             if visited[data[idx]]:
#                 result += len(cycle)
#                 break

#             idx = data[idx]
#             cnt += 1

#     print(result)


for _ in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        # 이미 싸이클에 포함된 학생
        if visited[i]:
            continue

        idx = i
        cycle = set()

        while True:
            visited[idx] = 1
            cycle.add(idx)
            if data[idx] in cycle:
                x = data[idx]
                while x in cycle:
                    cycle.remove(x)
                    x = data[x]
                result += len(cycle)
                break

            if visited[data[idx]]:
                result += len(cycle)
                break

            idx = data[idx]

    print(result)
                # print('cycle made')
                # print(cycle)
                # print('cycle not made')
                # print(cycle)