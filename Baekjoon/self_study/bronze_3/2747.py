###########################
#  BaekJoon 2747번
#  by 김승현                
###########################

# Q. 피보나치 수

n = int(input())

fibo = [0, 1]

for i in range(n-1):
    fibo.append(fibo[i]+fibo[i+1])
print(fibo[n])