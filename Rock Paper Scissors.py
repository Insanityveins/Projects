import random
import sys

choices = {
    "Rock": 1, "Paper": 2, "Scissors": 3
}



def translate(player):
    for choice, num in choices.items():
        if num == player:
            return choice

def battle(player, cpu):
    """
    Battle takes place.
    :param fighter:
    :return:
    """
    print("You chose {0} and the cpu chose {1}.".format(player, cpu))
    if player == "Rock" and cpu == "Scissors":
        print("You win!\n")
        main()
    elif player == "Rock" and cpu == "Paper":
        print("You lose!\n")
        main()
    elif player == cpu:
        print("It's a tie!\n")
        main()
    elif player == "Paper" and cpu == "Scissors":
        print("You lose!\n")
        main()
    elif player == "Paper" and cpu == "Rock":
        print("You win!\n")
        main()
    elif player == cpu:
        print("It's a tie!\n")
        main()
    elif player == "Scissors" and cpu == "Paper":
        print("You lose!\n")
        main()
    elif player == "Scissors" and cpu == "Rock":
        print("You lose!\n")
        main()
    elif player == cpu:
        print("It's a tie!\n")
        main()



def main():

    print("Welcome to rock, paper, scissors!!!")
    print("Rock = 1\n" "Paper = 2\n" "Scissors = 3\n" "Or enter 0 to end the game.\n")
    fighter = int(input("Choose your fighter: "))

    if fighter == 0:
        sys.exit(0)

    cpuChoice = random.randint(1,3)
    cpuString = translate(cpuChoice)
    playerString = translate(fighter)
    battle(playerString, cpuString)




if __name__ == "__main__":
    main()