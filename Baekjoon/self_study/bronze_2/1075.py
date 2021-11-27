###########################
#  BaekJoon 1075번
#  by 김승현                
###########################

# Q. 나누기

N, F = int(input()), int(input())

for i in range(100):
    if (N//100*100 + i)%F:
        continue
    print(str(i).zfill(2))
    break