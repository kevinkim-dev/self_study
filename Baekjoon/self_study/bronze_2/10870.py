###########################
#  BaekJoon 10870번
#  by 김승현                
###########################

# Q. 피보나치 수 5

N = int(input())
fibo1 = 0
fibo2 = 1
cnt = 1
while cnt < N:
    fibo1, fibo2 = fibo2, fibo1 + fibo2
    cnt += 1

if N == 0:
    print('0')
else:
    print(fibo2)
