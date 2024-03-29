wants_again = True

while wants_again:
    # NUMBER GUESSING GAME  => Угадай число
    import random
    lives = 7
    random_number = random.randint(1, 100)
    guessed_number = int(input("Enter a number from 1 to 100: "))

    while random_number != guessed_number:
        lives -= 1

        if guessed_number < random_number:
            print("Your number is too low!!!")
        elif guessed_number > random_number:
            print("Your number is too high!!!")

        if lives > 0:
            print(f"You have {lives} lives left.")
            guessed_number = int(input("Guess again: "))
        else:
            break

    def show_result(type):
        match type:
            case "win":
                print(f"You win!!!")
            case "lose":
                print(f"You lose!!!")


    if lives == 0:
        if random_number == guessed_number:
            show_result("win")
        else:
            show_result("lose")
            print(f'The number was {random_number}')
    elif random_number == guessed_number:
        show_result("win")
    else:
        show_result("lose")
        print(f'The number was {random_number}')

    print(f"You have {lives} lives left.")


    if input("Would you like to play again? (y/n): ") == "y":
        wants_again = True
    else:
        print("Goodbye!!!")
        wants_again = False