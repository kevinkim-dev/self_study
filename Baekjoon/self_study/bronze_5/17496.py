###########################
#  BaekJoon 17496번
#  by 김승현                
###########################

# Q. 스타후르츠

a, b, c, d = map(int, input().split())

print(c*((a-1) // b)*d)