###########################
#  BaekJoon 1934번
#  by 김승현                
###########################

# Q. 최소공배수

for _ in range(int(input())):
    a, b = map(int, input().split())
    tmp_a, tmp_b = a, b
    while tmp_a != tmp_b and max(tmp_a, tmp_b)%min(tmp_a, tmp_b) !=0:
        tmp_a, tmp_b = min(tmp_a, tmp_b), max(tmp_a, tmp_b)%min(tmp_a, tmp_b)
    print(a*b//min(tmp_a, tmp_b))