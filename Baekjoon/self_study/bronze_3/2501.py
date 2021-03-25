###########################
#  BaekJoon 2501번
#  by 김승현                
###########################

# Q. 약수 구하기

x, i = map(int, input().split())
p_list = []
for n in range(1, x+1):
    if x % n == 0:
        p_list.append(n)
print(p_list[i-1]) if len(p_list) >= i else print('0')