###########################
#  project_euler number 6
#  by 김승현                
###########################

# Q. 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?


N = 100
square_sum = 0
sum_square = 0


# 제곱의 합
for i in range(1, N+1):
    square_sum = square_sum + i * i


# 합의 제곱
for i in range(1, N+1):
    sum_square = sum_square + i

sum_square = sum_square * sum_square

if(sum_square >= square_sum):
    print(sum_square - square_sum)
else:
    print(square_sum - sum_square)