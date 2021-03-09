#########################
#  SWEA number 9700
#  by 김승현                
#########################

# Q. USB 꽂기의 미스터리

# s1: 한번 뒤집어서 꽂히려면 무조건 처음에 뒤집어서 꽂아보고 뒤집어서 꽂음
# s2: 두번 뒤집어서 꽂히려면 처음에 제대로 꽂아야가능

for t in range(1, int(input())+1):
    p, q = map(float, input().split())
    s1 = (1-p)*q
    s2 = p*(1-q)*q
    print("#%d YES" %t) if s1 < s2 else print("#%d NO" %t)
