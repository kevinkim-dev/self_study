###########################
#  BaekJoon 1076번
#  by 김승현                
###########################

# Q. 저항

color = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,

}

a, b, c = input(), input(), input()

print((color[a]*10 + color[b]) * 10**color[c])