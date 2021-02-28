###########################
#  BaekJoon 1193번
#  by 김승현                
###########################

# Q. 분수찾기

N = int(input())
x = 0
cnt = 0
while x < N:
    cnt += 1
    x += cnt

a = cnt - x + N
b = 1 + x - N
if (a+b) % 2 == 1:
    print("%d/%d" %(a, b))
else:
    print("%d/%d" %(b, a))