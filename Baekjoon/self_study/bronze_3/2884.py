###########################
#  BaekJoon 2884번
#  by 김승현                
###########################

# Q. 알람 시계

h, m = map(int, input().split())

time = h*60 + m - 45

if time < 0:
    time += 1440
new_m = time % 60
new_h = (time // 60) % 24

print(new_h, new_m)