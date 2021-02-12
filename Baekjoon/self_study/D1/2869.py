###########################
#  BaekJoon 2869번
#  by 김승현                
###########################

# Q. 달팽이는 올라가고 싶다.

up, down, height = map(int, input().split())

count = (height - down) // (up -down)

if (height - down) % (up -down) == 0:
    print(count)
else:
    print(count+1)