###########################
#  BaekJoon 9007번
#  by 김승현                
###########################

# Q. 카누 선수

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k, n = map(int, input().split())
    classes = []
    for _ in range(4):
        classes.append(list(map(int, input().split())))
    class12, class34 = [], []
    for i in range(n):
        for j in range(n):
            class12.append(classes[0][i] + classes[1][j])
            class34.append(classes[2][i] + classes[3][j])
    class12 = sorted(list(set(class12)))
    class34 = sorted(list(set(class34)))
    ans = 80000000
    for i in range(len(class12)):
        if ans == k:
            break
        a = class12[i]
        s, e = 0, len(class34) - 1
        while e - s > 1:
            m = (s + e) // 2
            if a + class34[m] > k:
                e = m - 1
            elif a + class34[m] < k:
                s = m
            else:
                ans = k
                break
        if abs(ans - k) > abs(a + class34[s] - k):
            ans = a + class34[s]
        elif abs(ans - k) == abs(a + class34[s] - k):
            ans = min(ans, a + class34[s])
        if len(class34) > 1:
            if abs(ans - k) > abs(a + class34[s+1] - k):
                ans = a + class34[s+1]
            elif abs(ans - k) == abs(a + class34[s+1] - k):
                ans = min(ans, a + class34[s+1])

    print(ans)

# import sys

# input = sys.stdin.readline

# for _ in range(int(input())):
#     k, n = map(int, input().split())
#     classes = []
#     for _ in range(4):
#         classes.append(list(map(int, input().split())))
#     class12, class34 = set(), set()
#     for i in range(n):
#         for j in range(n):
#             class12.add(classes[0][i] + classes[1][j])
#             class34.add(classes[2][i] + classes[3][j])
#     class12 = sorted(list(class12))
#     class34 = sorted(list(class34))
#     ans = 80000000
#     for i in range(len(class12)):
#         if ans == k:
#             break
#         a = class12[i]
#         s, e = 0, len(class34) - 1
#         while e - s > 1:
#             m = (s + e) // 2
#             if a + class34[m] > k:
#                 e = m - 1
#             elif a + class34[m] < k:
#                 s = m
#             else:
#                 ans = k
#                 break
#         if abs(ans - k) > abs(a + class34[s] - k):
#             ans = a + class34[s]
#         elif abs(ans - k) == abs(a + class34[s] - k):
#             ans = min(ans, a + class34[s])
#         if abs(ans - k) > abs(a + class34[s+1] - k):
#             ans = a + class34[s+1]
#         elif abs(ans - k) == abs(a + class34[s+1] - k):
#             ans = min(ans, a + class34[s+1])

#     print(ans)