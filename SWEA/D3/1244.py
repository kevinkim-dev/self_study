#########################
#  SWEA number 1244
#  by 김승현                
#########################

# Q. 최대 상금

# 한자리수를 바꿔주는 함수. DFS를 이용한다
def change(num, m):
    global max_price
    # 바꿔준 횟수와 바꿔줄 횟수가 같으면 max_price 갱신 후 return
    if m == M:
        max_price = max(max_price, int(''.join(map(str, num))))
        return
    # 최대 상금과 같아졌다면 남은 횟수를 보고 판단
    if num == max_num:
        # 같은 자리수가 없고, 남은 횟수가 홀수이면 1의 자리와 10의 자리가 바뀌는게 이상적
        if l == len(list(set(num))) and (M - m) % 2 == 1:
            num[-1], num[-2] = num[-2], num[-1]
        # 그것도 아니라면 그대로 갱신
        max_price = max(max_price, int(''.join(map(str, num))))
        return
    for i in range(l):
        # 앞자리부터 봤을때 max_num 과 다르다면 남은 숫자중 최대 숫자에 해당하는 숫자와 교체
        if num[i] != max_num[i]:
            max_change = max(num[i+1:])
            for j in range(i+1, l):
                if num[j] == max_change:
                    num[i], num[j] = num[j], num[i]
                    change(num, m+1)
                    num[i], num[j] = num[j], num[i]
            break
    return


for t in range(1, int(input())+1):
    num, M = map(int, input().split())
    num = list(map(int, (str(num))))
    max_num = sorted(num, reverse=True)
    l = len(num)
    max_price = 0
    change(num, 0)
    print("#%d %d" %(t, max_price))


# def change():
#     for i in range(len(num)):
#         if num[i] != max_num[i]:
#             max_change = max(num[i+1:])
#             for j in range(len(num)-1, i, -1):
#                 if num[j] == max_change:
#                     num[i], num[j] = num[j], num[i]
#                     return


# for t in range(1, int(input())+1):
#     num, T = map(int, input().split())
#     num = list(map(int, (str(num))))
#     max_num = sorted(num, reverse=True)
#     for t in range(T):
#         if num == max_num:
#             if len(num) == len(list(set(num))) and T - t % 2 == 0:
#                 num[-1], num[-2] = num[-2], num[-1]
#             break
#         change()
#         print(num)
#     print(num)