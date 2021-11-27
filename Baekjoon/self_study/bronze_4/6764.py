###########################
#  BaekJoon 6764번
#  by 김승현                
###########################

# Q. Sounds fishy!

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a < b < c < d:
    print("Fish Rising")
elif a > b > c > d:
    print("Fish Diving")
elif a == b and c == d and b == c:
    print("Fish At Constant Depth")
else:
    print("No Fish")