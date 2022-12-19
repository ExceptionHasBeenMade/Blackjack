import random
colorList = ["♠", "♥️", "♣️", "♦️"]
cards = []

while True:
    croupier = []
    player = []
    for number in range(13):
        for color in colorList:
            if(number > 8):
                if(number == 9):
                    figure = "Jack"
                elif(number == 10):
                    figure = "Queen"
                elif(number == 11):
                    figure = "King"
                elif(number == 12):
                    figure = "Ace"
                cards.append([str(figure) + color])
            else:
                cards.append([str(number+2) + color])
    croupier = random.choices(cards, k = 2)
    if(croupier[0] == croupier[1]):
        continue
    cards.remove(croupier[0])
    cards.remove(croupier[1])
    player = random.choices(cards, k = 2)
    if(player[0] == player[1]):
        continue
    cards.remove(player[0])
    cards.remove(player[1])
    while True:
        print("Croupier's cards:")
        print(croupier[0])
        print("")
        print("Your's cards:")
        print(player[0])
        print(player[1])
        print("")
        decision = input("What do you want to do(Hit/Stand): ")
        decision = decision.lower()
        if(decision == "hit" or decision == "h"):
            pass
        elif(decision == "stand" or decision == "s"):
            pass


# test_list = [11, 44, 55, 22, 77]
# print("Original list is : " + str(test_list))
#  
# print("Random element is :", random.choices(test_list, k=4))