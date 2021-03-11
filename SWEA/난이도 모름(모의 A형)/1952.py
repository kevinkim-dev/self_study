#########################
#  SWEA number 1952
#  by 김승현                
#########################

# Q. 수영장

# 사용방법은 day, 1 month, 3 month
# day -> swims[month-1]*day, month -= 1
# month -> m_1, month -= 1
# 3 month -> m_3, month -= 3
# 자료구조: 12월, 0원에서 시작
# 1. 가격이 min_cost보다 높아지면 return
# 2. 1~3월에서 연산이 끝나면 min(min_cost, cost)

# # 느리네...

# def swim_pay(min_cost):
#     while q:
#         cost, month = q.pop(0)
#         if cost >= min_cost:
#             continue
#         elif month >= 13:
#             min_cost = cost
#             continue
#         q.append((cost+swim[month]*day, month+1))
#         q.append((cost+m_1, month+1))
#         q.append((cost+m_3, month+3))
#     return min_cost
        
# for t in range(1, int(input())+1):
#     day, m_1, m_3, year = map(int, input().split())
#     swim = [0] + list(map(int, input().split()))
#     q = [(0, 1)]
#     print("#%d %d" %(t, swim_pay(year)))
        
for t in range(1, int(input())+1):
    day, m_1, m_3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split())) + [0, 0]
    swim_pay = [0]*15
    for month in range(1, 15):
        if month >= 3:
            swim_pay[month] = min(swim_pay[month-1]+day*swim[month], swim_pay[month-1]+m_1, swim_pay[month-3]+m_3)
        else:
            swim_pay[month] = min(swim_pay[month-1]+day*swim[month], swim_pay[month-1]+m_1)
    print("#%d %d" %(t, min(swim_pay[12], swim_pay[13], swim_pay[14], year)))