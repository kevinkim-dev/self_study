###########################
#  project_euler number 2  
#  by 김승현                
###########################

# Q. 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합

total = 0

fib1 = 1
fib2 = 2

while fib1 <= 4000000:
    if(fib1 % 2 == 0):
        total = total + fib1
    fib1, fib2 = fib2, fib1 + fib2

print(total)