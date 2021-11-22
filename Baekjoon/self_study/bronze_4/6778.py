###########################
#  BaekJoon 6778번
#  by 김승현                
###########################

# Q. Which Alien?

ant, eye = int(input()), int(input())

alien_list = []

if ant >= 3 and eye <= 4:
    alien_list.append('TroyMartian')
if ant <= 6 and eye >= 2:
    alien_list.append('VladSaturnian')
if ant <= 2 and eye <= 3:
    alien_list.append('GraemeMercurian')

for alien in alien_list:
    print(alien)