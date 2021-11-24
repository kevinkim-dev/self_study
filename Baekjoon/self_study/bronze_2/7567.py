###########################
#  BaekJoon 7567번
#  by 김승현                
###########################

# Q. 그릇

plates = input()

ans, start = 0, ''
for plate in plates:
    if plate == start:
        ans += 5
    else:
        ans += 10
        start = plate

print(ans)