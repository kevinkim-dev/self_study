###########################
#  BaekJoon 13301번
#  by 김승현                
###########################

# Q. 타일 장식물

N = int(input())

fibo = [0, 1]
for i in range(N):
    fibo.append(fibo[-1]+fibo[-2])
print(2*(fibo[-1]+fibo[-2]))