import random
import time


def generate_sequence():
    global difficulty_level_answer
    global random_list
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

    random_list = random.sample(range(1, 102), difficulty_level_answer)
    print("Remember the numbers")
    time.sleep(1)
    print(random_list, end="")
    time.sleep(1.7)
    print("\r", end="")


def get_list_from_user():
    global user_list
    user_list = list(int(num) for num in
                     input(
                         "Enter " + str(difficulty_level_answer) + " numbers separated by space: \n").strip().split())[
                :difficulty_level_answer]
    print("User List: ", user_list)


def is_list_equal():
    if random_list == user_list:
        print("You won the game")
    else:
        print("You lost the game")


def play_Memory_Game():
    generate_sequence()
    get_list_from_user()
    is_list_equal()
