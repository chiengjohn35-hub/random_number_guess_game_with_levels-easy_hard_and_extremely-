
# author : Chieng John
# created : 9/16/2025



#number guessing game
import random
import sys

#define game levels (easy, hard and extremely)
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

    #random number between (3-12)
    num = random.randint(3,12)

    #user input to ask the level of the game and call that function defined up there amd replace the parameter
    # with this user input level. then create a local variable as  named down below (chances), each level has
    # its own chances: then we go loop through all the chances and remind the user how many the left with while guessing the right number
    level = input("enter the level of the game (easy, hard and extremely) :").strip()
    chances = level_of_game(level)

    print(f"You have {chances} chances to guess the right num between (3-12) ")
    while chances>0:

        #use try and except to handle all the errors
        try:
            play = int(input("Enter a digit!  :"))

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
        except ValueError:
            print("Please Your digit must be a number")


if __name__=="__main__":
    main()
    #create a user input to ask if they want play again after the loop ended, if so call the main function else
    #use sys.exit() to exit the game
    while True:
        play_again=input("do you want to play again? (YES/NO) :").strip()
        if play_again.lower().startswith("y"):
            main()
        else:
            sys.exit("Thanks for playing, Have a nice day!")
        

