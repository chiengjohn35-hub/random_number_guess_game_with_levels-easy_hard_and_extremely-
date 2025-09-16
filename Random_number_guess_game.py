#number guessing game

import random


def level_of_game( level):

    if level =="easy":
        num_of_guess = 9
        return num_of_guess
    elif level=="hard":
        num_of_guess=6
        return num_of_guess
    else:
        num_of_guess = 4
        return num_of_guess

def main():
    num = random.randint(3,12)
    level = input("enter the level of the game (easy, hard and extremely) :").strip()
    chances = level_of_game(level)

    print(f"You have {chances} chances to guess the right num between (3-12) ")
    while chances>0:
        play = int(input("Enter a digit!"))

        if play<3:
            print("Too low!")
            continue
        elif play>12:
            print("Too high!")
            continue

        if play==num:
            print("You win!")
            break
        else:
            chances-=1
            print("Try again!")
            print(f"You have {chances} chances left!")
            if chances<=0:
                print("Game Over!")
                break

        # play_again=input("do you want to play again? (YES/NO)").strip()
        # if play_again.lower().startswith("y"):
        #         continue
        # else:
        #     break
    print(sep="     ")
    print("Thanks for playing, Have a nice day!")

if __name__=="__main__":
    main()