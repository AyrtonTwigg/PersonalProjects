import random

WIN_SCORE = 100
player_total = 0
AI_total = 0
turn = random.choice([1,-1])

while player_total < WIN_SCORE and AI_total < WIN_SCORE:
    user_choice = 'Y'

    if turn > 0:
        print("----------NEW TURN----------")
        temp = 0
        while user_choice != 'N':
            roll = random.randint(1, 6)
            if roll == 1:
                print("*******YOU ROLLED A 1: SCORED 0*******")
                temp = 0
                break
            temp += roll

            print("SCORE PLAYER: %d" %player_total)
            print("SCORE AI: %d" %AI_total)
            print("YOU ROLLED %d MAKING A TOTAL OF: %d" %(roll, temp))
            user_choice = input("TYPE 'N' TO STOP ROLLING\n")
        player_total += temp
        turn *= -1

    elif turn < 0:
        temp = 0
        while True:
            roll = random.randint(1, 6)
            if roll == 1:
                print("*******AI ROLLED A 1*******")
                temp = 0
                break
            temp += roll
            print("AI ROLLED %d MAKING A TOTAL OF: %d" %(roll, temp))
            if (AI_total + temp) > WIN_SCORE:
                break
            if (WIN_SCORE - (AI_total + temp)) < 13:
                continue
            if (WIN_SCORE - player_total) < 18:
                if (WIN_SCORE - player_total) < 8:
                    continue
                if temp > 50:
                    break
                continue
            if (AI_total + temp - player_total) > 25 and temp > 16:
                break
            if temp / 2 >= (player_total - temp) and temp > 30:
                break
            if temp > 21:
                if player_total < WIN_SCORE / 2 and (AI_total + temp - player_total) > -16:
                    break
                elif player_total < WIN_SCORE * (3 / 4) and (AI_total + temp - player_total) > -7:
                    break

        print("AI STOPPED, SCORING: %d\n" %temp)
        AI_total += temp
        turn *= -1

if AI_total >= 100:
    print("*****AI WINS WITH A TOTAL OF: %d-%d*****" %(AI_total,player_total))
else:
    print("******CONGRATULATIONS!!!! YOU WON WITH A SCORE OF: %d-%d******" %(player_total,AI_total))
