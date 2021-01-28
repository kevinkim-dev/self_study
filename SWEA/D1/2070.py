#########################
#  SWEA number 2070  
#  by 김승현                
#########################

# Q. 큰 놈, 작은 놈, 같은 놈

for test_case in range(int(input())):
    num_list = list(map(int, input().split()))
    print(f"#{test_case + 1}", end = ' ')
    if num_list[0] > num_list[1]:
        print(">")
    elif num_list[0] < num_list[1]:
        print("<")
    else:
        print("=")