###########################
#  BaekJoon 10984번
#  by 김승현                
###########################

# Q. 내 학점을 구해줘

for _ in range(int(input())):
    x, y = 0, 0
    for _ in range(int(input())):
        a, b = input().split()
        x += int(a)
        y += int(a) * float(b)
    print(x, y/x)