import random

def num_guessing_game():
    secreat_numbeer= random.randint(1,100)
    attempts = 0
    max_attempts = 5

    print("number guessing game ")
    print(f"i am thinking a number between 1 to 100 . you have {max_attempts} attempts.\n")

    while attempts < max_attempts :
        try:
            guess = int(input("enter your guess : "))
            attempts+=1
            if guess > secreat_numbeer :
                print(" too high 😠!, try a lower number.\n")

            elif guess<secreat_numbeer :
                print("too low 🙁!,try a higher number .\n")

            else :
                print(f"congratulation🤩! you guessed the number {secreat_numbeer} in { attempts} attempts. ")
                break
        except ValueError:
            print("invalid input.please enter a whole number.")
    else:
        print(f"sorry you ran out of attempts. the secreat number was {secreat_numbeer}.")

num_guessing_game()
