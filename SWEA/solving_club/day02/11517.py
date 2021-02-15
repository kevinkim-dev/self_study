T = int(input())

for t in range(1, T+1):
    card_num = int(input())
    card_string = input()

    card_count = [0]*10
    for i in range(card_num):
        card_count[int(card_string[i])] += 1
    max_count = 0
    max_count_card = 0
    for card in range(10):
        if card_count[card] >= max_count:
            max_count = card_count[card]
            max_count_card = card

    print("#%d %d %d" % (t, max_count_card, max_count))
    