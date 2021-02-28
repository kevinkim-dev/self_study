###########################
#  BaekJoon 14173번
#  by 김승현                
###########################

# Q. Square Pasture

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(max(abs(x4-x1), abs(x2-x3), abs(y4-y1), abs(y2-y3), x2-x1, y2-y1, x4-x3, y4-y3)**2)