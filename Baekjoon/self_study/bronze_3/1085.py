###########################
#  BaekJoon 1085번
#  by 김승현                
###########################

# Q. 직사각형에서 탈출

x, y, width, height = map(int, input().split())

print(min(x, width-x, y, height-y))