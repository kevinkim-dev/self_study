###########################
#  project_euler number 16
#  by 김승현                
###########################

# Q. 2^1000의 각 자릿수를 모두 더하면?

N = 2 ** 1000

sum = 0

while N > 0:
    sum = sum + N % 10
    N = N // 10

print(sum)