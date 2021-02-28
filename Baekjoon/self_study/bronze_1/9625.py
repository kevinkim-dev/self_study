###########################
#  BaekJoon 9625번
#  by 김승현                
###########################

# Q. BABBA

# A의 갯수는 B의 갯수
# B의 갯수는 A의 갯수 + B 의 갯수

a = 1
b = 0

t = int(input())
for _ in range(t):
    a, b = b, a + b

print(a, b)