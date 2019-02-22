import random


def Move(my_total, opp_total, WIN_SCORE):
    temp_total = 0
    num_rolls = 0

    while True:
        roll = random.randint(1, 6)
        if roll == 1:
            return 0
        else:
            temp_total += roll
        num_rolls += 1
        if (my_total + temp_total) > WIN_SCORE:
            return temp_total
        # ABOVE CODE SHOULD NOT CHANGE

        if (WIN_SCORE - (my_total + temp_total)) < 13:
            continue
        if (my_total + temp_total) > WIN_SCORE*3/4 and (my_total + temp_total - opp_total) > 45 and temp_total > 12:
            break
        if (WIN_SCORE - opp_total) < 18:
            if (WIN_SCORE - opp_total) < 8:
                continue
            if temp_total > 50:
                break
            continue

        if (my_total + temp_total - opp_total) > 25 and temp_total > 16:
            break

        if temp_total/2 >= (opp_total - temp_total) and temp_total > 30:
            break

        if temp_total > 21:
            if opp_total < WIN_SCORE/2 and (my_total + temp_total - opp_total) > -16:
                break
            elif opp_total < WIN_SCORE*(3/4) and (my_total + temp_total - opp_total) > -7:
                break


    return temp_total
