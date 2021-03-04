###########################
#  BaekJoon 5928번
#  by 김승현                
###########################

# Q. Contest Timing

x = 11 * 24 * 60 + 11 * 60 + 11
d, h, m = map(int, input().split())
y = d * 24 * 60 + h * 60 + m
print('-1') if y < x else print(y-x)