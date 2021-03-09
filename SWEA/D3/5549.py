#########################
#  SWEA number 5549
#  by 김승현                
#########################

# Q. 홀수일까 짝수일까
 
for t in range(1, int(input())+1):
    print("#%d Odd" %t) if int(input()[-1]) % 2 == 1 else print("#%d Even" %t)