###########################
#  BaekJoon 2752번
#  by 김승현                
###########################

# Q. 세수 정렬

a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)