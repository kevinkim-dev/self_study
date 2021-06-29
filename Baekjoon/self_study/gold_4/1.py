import time

def function1():
    return 

# def function2(x):
#     if x == N:
#         return x
#     return function2(x+1)

N = 100000000
start_time = time.time()
for _ in range(N):
    function1()
fin_time = time.time()
print(start_time*10000)
print(fin_time*10000)
print(f'main과 함수를 왔다갔다하는 경우 : {fin_time-start_time}')
# start_time = time.time()
# function2(0)
# fin_time = time.time()
# print(f'함수에서만 연산하는 경우 : {fin_time-start_time}')
# x = 1

# start_time = time.time()
# for _ in range(N):
#     x += 1
# fin_time = time.time()
# print(start_time)
# print(fin_time)
# print(f'main과 함수를 왔다갔다하는 경우 : {fin_time-start_time}')