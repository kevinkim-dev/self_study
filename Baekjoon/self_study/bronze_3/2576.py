###########################
#  BaekJoon 2576번
#  by 김승현                
###########################

# Q. 홀수

odd = []

for _ in range(7):
    x = int(input())
    if x % 2 == 1:
        odd.append(x)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print('-1')