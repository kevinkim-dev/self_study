###########################
#  BaekJoon 11022번
#  by 김승현                
###########################

# Q. A+B - 8

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(t, a, b, a+b))