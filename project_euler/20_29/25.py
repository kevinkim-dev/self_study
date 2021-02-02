# ##########################
#  project_euler number 25
#  by 김승현                
# ##########################

# Q. 피보나치 수열에서 처음으로 1000자리가 되는 항은 몇 번째?

fib_1 = 1
fib_2 = 1
fib_result = 0
count = 2
while len(str(fib_result)) < 1000:
    fib_result = fib_1 + fib_2
    fib_1, fib_2 = fib_2, fib_result
    count += 1

print(fib_result, count)

