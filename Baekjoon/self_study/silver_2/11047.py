###########################
#  BaekJoon 11047번
#  by 김승현                
###########################

# Q. 동전 0

num_coin, money = map(int, input().split())

coin_list = [0]*num_coin
coin_count = 0
for i in range(num_coin):
    coin_list[i] = int(input())

for n in range(num_coin-1, -1, -1):
    coin_count += money // coin_list[n]
    money = money % coin_list[n]

print(coin_count)