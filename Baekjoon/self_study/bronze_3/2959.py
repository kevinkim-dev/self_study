###########################
#  BaekJoon 2959번
#  by 김승현                
###########################

# Q. 거북이

a, b, c, d = sorted(list(map(int, input().split())))

print(min(a,b)*min(c,d))