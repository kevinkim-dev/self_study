###########################
#  BaekJoon 15726번
#  by 김승현                
###########################

# Q. 이칙연산

a, b, c = map(int, input().split())

print(int(a*b/c)) if b > c else print(int(a/b*c))