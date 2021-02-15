###########################
#  BaekJoon 14924번
#  by 김승현                
###########################

# Q. 폰 노이만과 파리

train, fly, length = map(int, input().split())

print(int(fly * (length / (2 * train))))