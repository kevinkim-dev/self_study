###########################
#  BaekJoon 1158번
#  by 김승현                
###########################

# Q. 요세푸스 문제

n, k = map(int, input().split())

yo_list = list(range(1, n+1))

idx, k = 0, k-1
ans = []

while yo_list:
    idx += k
    if idx >= len(yo_list):
        idx %= len(yo_list)
    ans.append(str(yo_list.pop(idx)))

print('<' + ', '.join(ans) + '>')
