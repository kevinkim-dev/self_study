# ##########################
#  project_euler number 20
#  by 김승현                
# ##########################

# Q. 100! 의 자릿수를 모두 더하면?

fact = 1
for i in range(1, 101):
    fact *= i

count = 0
while fact > 0:
    count += fact % 10
    fact //= 10

print(count)