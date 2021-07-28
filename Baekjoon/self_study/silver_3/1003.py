###########################
#  BaekJoon 1003번
#  by 김승현                
###########################

# Q. 피보나치 함수

fibo = [[1, 0], [0, 1]]

for _ in range(40):
    fibo.append([fibo[-1][0] + fibo[-2][0], fibo[-1][1] + fibo[-2][1]])

for _ in range(int(input())):
    x = int(input())
    print(fibo[x][0], fibo[x][1])