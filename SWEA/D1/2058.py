#########################
#  SWEA number 2058  
#  by 김승현                
#########################

# Q. 자릿수 더하기

n = int(input())

total = 0
while n > 0:
    total += n % 10
    n //= 10
    
print(total)