###########################
#  BaekJoon 2775번
#  by 김승현                
###########################

# Q. 부녀회장이 될테야

for t in range(1, int(input())+1):
    k, n = int(input()), int(input())
    apartment = [[1] + [0]*14 for _ in range(15)]
    apartment[0] = list(range(1, 15))
    for i in range(1, 15):
        for j in range(0, 14):
            apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]
    print(apartment[k][n-1])

