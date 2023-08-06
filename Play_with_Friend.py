instruction = '''
Tic Tac Toe insruction Board
You can choose any number between 1-9

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
'''
sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')


def print_board():
    board = f'''

     {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
    ---|---|---
     {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
    ---|---|---
     {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}

'''
    print(board)


index_list = []


def take_input(player_name):
    while True:
        X = int(input(f"{player_name} : "))
        X -= 1
        if 0 <= X < 10:
            if X in index_list:
                print("This spotted is bloked.")
                continue
            index_list.append(X)
            return X
        print("please enter number between 1-9")


def calculate_result(player_1, player_2):

    if (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == "X") or (sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == "X") or (sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == "X") or (sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == "X") or (sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == "X") or (sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == "X") or (sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == "X") or (sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == "X"):
        print(f"Congratulation ! {player_1} win !!!")
        quit("Thanks for joining")
    elif (sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == "O") or (sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == "O") or (sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == "O") or (sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == "O") or (sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == "O") or (sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == "O") or (sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == "O") or (sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == "O"):
        print(f"Congratulation ! {player_2} win !!!")
        quit("Thanks for joining")


def main():

    # Step-1 Instruction

    print("\nWelcome in tic tac toe !\n")
    player_1 = input("Enter ur name : ")
    player_2 = input("Enter ur name : ")
    print(f"Thank you for joining the game {player_1} and {player_2}.")
    print(instruction)
    print(f"{player_1} sign will be : X ")
    print(f"{player_2} sign will be : O ")

    input("Enter any key to start the game")

    # step-2 print board
    print_board()

    # step-3 take input
    for i in range(9):
        if (i % 2 == 0):
            index = take_input(player_1)
            sign_dictionary[index] = "X"
        else:
            index = take_input(player_2)
            sign_dictionary[index] = "O"

        print_board()

    # step-4 result
        calculate_result(player_1, player_2)
    print("This a TIE,")


main()
