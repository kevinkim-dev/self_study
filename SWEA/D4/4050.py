#########################
#  SWEA number 4050
#  by 김승현                
#########################

# Q. 재관이의 대량 할인

for t in range(1, int(input())+1):
    N = int(input())
    price_list = sorted(list(map(int, input().split())), reverse=True)
    ans = sum(price_list) - sum(price_list[2::3])
    print("#%d %d" %(t, ans))
