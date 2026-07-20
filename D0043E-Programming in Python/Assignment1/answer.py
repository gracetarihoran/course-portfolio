import random

'''
Dice Game 12
Author: Grace Tarihoran
'''


TARGET = 12
DICE_MIN = 1
DICE_MAX = 6


# Print welcome text
def print_welcome():
    print("Welcome to dice game 12!", end=" ")
    print("You must roll 1-3 dice and try to get the sum of 12.")


# Rolling dice
def roll_dice():
    dice_number = random.randint(DICE_MIN, DICE_MAX)
    return dice_number


# Show status: sums, wins and losses total
def show_state(_d1, _d2, _d3, _wins, _losses):
    _total = _d1 + _d2 + _d3
    print(f"{_d1} {_d2} {_d3} sum: {_total} #win: {_wins} #loss: {_losses}")


# Read choice from input and return q, 1, 2, 3. Check if dice has been rolled before.
def read_choice(_rolled1, _rolled2, _rolled3):
    while True:
        _choice = input("Enter which dice you want to roll [1,2,3] (exit with q): ")

        if _choice == 'q':
            return 'q'

        if not _choice.isdigit():
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q\n")
            continue

        _choice = int(_choice)

        if _choice < 1 or _choice > 3:
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q")
            continue

        if _choice == 1:
            if _rolled1 is True:
                print("Sorry, you have already rolled that dice. Try again")
                continue

            _rolled1 = True

        elif _choice == 2:
            if _rolled2 is True:
                print("Sorry, you have already rolled that dice. Try again")
                continue

            _rolled2 = True

        else:
            if _rolled3 is True:
                print("Sorry, you have already rolled that dice. Try again")
                continue

            _rolled3 = True

        return _choice


# Run each round, 1 time for every dice
def play_round(_win, _loss):
    d1 = 0
    d2 = 0
    d3 = 0
    rolls_done = 0
    total = 0
    rolled1 = False
    rolled2 = False
    rolled3 = False

    while rolls_done < 3:
        choice = read_choice(rolled1, rolled2, rolled3)

        if choice == 'q':
            return "quit"

        if choice == 1:
            d1 = roll_dice()
            rolled1 = True
        elif choice == 2:
            d2 = roll_dice()
            rolled2 = True
        else:
            d3 = roll_dice()
            rolled3 = True

        rolls_done += 1

        if rolls_done < 3:
            show_state(d1, d2, d3, _win, _loss)
        else:
            total = d1 + d2 + d3
            if total == TARGET:
                _win = _win + 1
                show_state(d1, d2, d3, _win, _loss)
                print("You won!!")
                return "win"
            elif total > TARGET:
                _loss = _loss + 1
                show_state(d1, d2, d3, _win, _loss)
                print("You lost!!")
                return "loss"
            else:
                show_state(d1, d2, d3, _win, _loss)
                print("You neither won nor lost the game.")
                return "none"


# Main program always loop until user quit the game
def main():
    print_welcome()

    wins = 0
    losses = 0

    while True:
        round_state = play_round(wins, losses)

        if round_state == "quit":
            print(f"#win: {wins} #loss: {losses}")
            print("Game Over!")
            break
        elif round_state == "win":
            wins = wins + 1
        elif round_state == "loss":
            losses = losses + 1

        print("\nNext round!\n")
        continue


# Main guard
if __name__ == '__main__':
    main()
