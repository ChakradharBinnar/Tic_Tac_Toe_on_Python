import random

print("\nWelcome in tic tac toe\n")

player1 = input("Enter Your name : ")
player2 = "Computer"

instruction = '''

Instuctions:
You can choose any index number between 1-9
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
 
'''

sign_dict = []
for i in range(1, 11):
    sign_dict.append(' ')


def printBoard():
    Board = f'''

      {sign_dict[1]} | {sign_dict[2]} | {sign_dict[3]}
     ---|---|---
      {sign_dict[4]} | {sign_dict[5]} | {sign_dict[6]}
     ---|---|---
      {sign_dict[7]} | {sign_dict[8]} | {sign_dict[9]}

'''
    print(Board)


index_list = []


def take_input(player):
    while True:
        x = int(input(f"{player} : "))
        if 0 <= x < 10:
            if x in index_list:
                print("Block is not vaccant")
                print("Plzz choose another index number")
                continue
            index_list.append(x)
            return x
        print("Plzz choose number between 1-9")


def random_num():
    while True:
        y = random.randint(1, 10)
        if 0 <= y < 10:
            if y in index_list:
                print("Block is not vaccant")
                print("Plzz choose another index number")
                continue
            index_list.append(y)
            return y
        print("Plzz choose number between 1-9")


def check_result(player1, player2):
    if (sign_dict[1] == sign_dict[2] == sign_dict[3] == "X") or (sign_dict[4] == sign_dict[5] == sign_dict[6] == "X") or (sign_dict[7] == sign_dict[8] == sign_dict[9] == "X") or (sign_dict[1] == sign_dict[4] == sign_dict[7] == "X") or (sign_dict[2] == sign_dict[5] == sign_dict[8] == "X") or (sign_dict[3] == sign_dict[6] == sign_dict[9] == "X") or (sign_dict[1] == sign_dict[5] == sign_dict[9] == "X") or (sign_dict[3] == sign_dict[5] == sign_dict[7] == "X"):
        quit(f"Congratulation ! {player1} win the game !")

    elif (sign_dict[1] == sign_dict[2] == sign_dict[3] == "O") or (sign_dict[4] == sign_dict[5] == sign_dict[6] == "O") or (sign_dict[7] == sign_dict[8] == sign_dict[9] == "O") or (sign_dict[1] == sign_dict[4] == sign_dict[7] == "O") or (sign_dict[2] == sign_dict[5] == sign_dict[8] == "O") or (sign_dict[3] == sign_dict[6] == sign_dict[9] == "O") or (sign_dict[1] == sign_dict[5] == sign_dict[9] == "O") or (sign_dict[3] == sign_dict[5] == sign_dict[7] == "O"):
        quit(f"Computer win the game !")


def main():
    print(f"\nThank you {player1} joining the game.")
    print(instruction)
    print(f"{player1} sign -> X ")
    print(f"Computer sign -> O ")

    input("press enter to start game : ")
    printBoard()

    for i in range(1, 10):
        if (i % 2 != 0):
            index = take_input(player1)
            sign_dict[index] = "X"
        else:
            index = random_num()
            sign_dict[index] = "O"
        printBoard()
        check_result(player1, player2)
    print("Game is Tie !")


main()
