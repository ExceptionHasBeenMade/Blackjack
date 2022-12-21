import random, os
colorList = ["♠️", "♥️", "♣️", "♦️"]
cards = []
stood = False

def resultCounting(variable, croupier = False):
    result = 0
    for card in variable:
        for item in card:
            i = item[0]
            try:
                if(i == "1"):
                    i = 10
                result = result + int(i)
            except ValueError:
                if(i == "♠️" or i == "♥️" or i == "♣️" or i == "♦️"):
                    break
                else:
                    if(i == "J" or i == "Q" or i == "K"):
                        i = 10
                    elif(i == "A"):
                        if(result < 11):
                            i = 10
                        else:
                            i = 1
                result = result + i
        if(croupier):
            break
    return result

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
        os.system("cls")
        print("Croupier's card:")
        if(stood):
            pass
        else:
            print(croupier[0][0])
        print("")
        print("Croupier total is " + str(resultCounting(croupier, croupier=True)))
        print("")
        print("Your's cards:")
        for card in player:
            print(card[0])
        print("")
        print("Your total is " + str(resultCounting(player)))
        print("")
        if(stood == False):
            decision = input("What do you want to do(Hit/Stand): ")
            decision = decision.lower()
        if(decision == "stand" or decision == "s"):
            stood = True
        elif(decision == "hit" or decision == "h"):
            work = random.choice(cards)
            player.append(work)
            cards.remove(work)
        if(resultCounting(player) > 21):
            print("You lose")
            input()
            break
