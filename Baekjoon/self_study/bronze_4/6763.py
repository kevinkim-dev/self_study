###########################
#  BaekJoon 6763번
#  by 김승현                
###########################

# Q. Speed fines are not fine!

speed = -(int(input()) - int(input()))

if speed <= 0:
    print("Congratulations, you are within the speed limit!")
elif speed <= 20:
    print("You are speeding and your fine is $100.")
elif speed <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")