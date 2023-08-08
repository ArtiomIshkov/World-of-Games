import random



def generate_number():
    global difficulty_level_answer
    print("Please choose game difficulty from 1 to 5:")
    while True:
        try:
            difficulty_level_answer = int(input())
        except ValueError:
            print("Please enter valid number from 1 to 5:")
            continue
        else:
            break

    while difficulty_level_answer < 1 or difficulty_level_answer > 5:
        try:
            difficulty_level_answer = int(input("Please enter valid number from 1 to 5:"))
        except ValueError:
            print("Please enter valid number from 1 to 5:")
        if difficulty_level_answer == 1:
            difficulty_level_answer = 1
        elif difficulty_level_answer == 2:
            difficulty_level_answer = 2
        elif difficulty_level_answer == 3:
            difficulty_level_answer = 3
        elif difficulty_level_answer == 4:
            difficulty_level_answer = 4
        elif difficulty_level_answer == 5:
            difficulty_level_answer = 5
    global secret_number
    secret_number = random.randint(1, difficulty_level_answer)


def get_guess_from_user():
    print("Take a guess between 1 to " + str(difficulty_level_answer))
    global guess
    guess = input()
    guess = int(guess)


def compare_results():
    if guess == secret_number:
        print("Correct Answer")

    if guess != secret_number:
        number = str(secret_number)
        print("wrong answer, was thinking of" + number)


def play_guess_game():
    generate_number()
    get_guess_from_user()
    compare_results()
#exit
