###########################
#  project_euler number 3 
#  by 김승현                
###########################

# Q. 가장 큰 소인수 구하기

N = 600851475143
div = 2

# 소수 찾기

while N != 1:
    if N % div == 0:
        N = N / div
    else:
        div = div + 1

print(div)