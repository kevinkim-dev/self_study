###########################
#  BaekJoon 2908번
#  by 김승현                
###########################

# Q. 상수

a, b = input().split()

a_rev = int(a[::-1])
b_rev = int(b[::-1])

print(a_rev) if a_rev > b_rev else print(b_rev)