#########################
#  SWEA number 1933  
#  by 김승현                
#########################

# Q. 간단한 N 의 약수

n = int(input())
div_list = []
 
for i in range(1, n+1):
    if n % i == 0:
        div_list.append(i)
 
print(*div_list)