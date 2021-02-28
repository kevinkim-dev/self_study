###########################
#  BaekJoon 16199번
#  by 김승현                
###########################

# Q. 나이 계산하기

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

a, b, c = y2-y1, y2-y1+1, y2-y1
if m1 > m2 or (m1 == m2 and d1 > d2):
    a -= 1

print(a)
print(b)
print(c)