###########################
#  BaekJoon 19698번
#  by 김승현                
###########################

# Q. 헛간 청약

n, w, h, l = map(int, input().split())
max_cow = (w//l) * (h//l)
print(max_cow) if max_cow <= n else print(n)