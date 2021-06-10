# GENERAL ERRORS
"""
- UnboundLocalError: local variable 'j' referenced before assignment
"""
# MAIN BUGS
"""
- cant check an ola ta boxes einai full alla last move wins vgazei it's a tie or winner
"""
from random import seed
from random import randrange
from datetime import datetime

# ΔΗΜΙΟΥΡΓΙΑ ΠΛΑΙΣΙΟΥ
playground_list_ref = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

playground_list = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def print_playground():
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list[0][0]} ", end="")
    print(f"| {playground_list[0][1]} ", end="")
    print(f"| {playground_list[0][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list[1][0]} ", end="")
    print(f"| {playground_list[1][1]} ", end="")
    print(f"| {playground_list[1][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list[2][0]} ", end="")
    print(f"| {playground_list[2][1]} ", end="")
    print(f"| {playground_list[2][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")


def print_playground_ref():
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list_ref[0][0]} ", end="")
    print(f"| {playground_list_ref[0][1]} ", end="")
    print(f"| {playground_list_ref[0][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list_ref[1][0]} ", end="")
    print(f"| {playground_list_ref[1][1]} ", end="")
    print(f"| {playground_list_ref[1][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")
    print("  ", end="")
    print(f"| {playground_list_ref[2][0]} ", end="")
    print(f"| {playground_list_ref[2][1]} ", end="")
    print(f"| {playground_list_ref[2][2]} ", end="")
    print("|   ")
    print("  +", end="")
    print("-" * 11, end="")
    print("+")


def winner_check(player, computer):
    global winner
    if player_choice == computer_choice:
        print(f"Computer played {computer_choice}. ", end="")
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "paper":
        print(f"Computer played {computer_choice}.")
        print("Computer wins!", end=" ")
        print("You play second!")
        winner = "computer"
    elif player_choice == "rock" and computer_choice == "scissors":
        print(f"Computer played {computer_choice}.")
        print("You win!", end=" ")
        print("You play first!")
        winner = "player"
    elif player_choice == "paper" and computer_choice == "scissors":
        print(f"Computer played {computer_choice}.")
        print("Computer wins!", end=" ")
        print("You play second!")
        winner = "computer"
    elif player_choice == "paper" and computer_choice == "rock":
        print(f"Computer played {computer_choice}.")
        print("You win!", end=" ")
        print("You play first!")
        winner = "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        print(f"Computer played {computer_choice}.")
        print("You win!", end=" ")
        print("You play first!")
        winner = "player"
    elif player_choice == "scissors" and computer_choice == "rock":
        print(f"Computer played {computer_choice}.")
        print("Computer wins!", end=" ")
        print("You play second!")
        winner = "computer"
    else:
        print("Non valid entry!")


def player_plays():
    player_box = input("Choose your box(type numbers 1-9): ").strip()
    if player_box != "1" and player_box != "2" and player_box != "3" and player_box != "4" and player_box != "5" and player_box != "6" and player_box != "7" and player_box != "8" and player_box != "9":
        print("Invalid entry, try again!")
        player_plays()
    else:
        if player_box == "1":
            if playground_list[0][0] == " ":
                playground_list[0][0] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "2":
            if playground_list[0][1] == " ":
                playground_list[0][1] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "3":
            if playground_list[0][2] == " ":
                playground_list[0][2] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "4":
            if playground_list[1][0] == " ":
                playground_list[1][0] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "5":
            if playground_list[1][1] == " ":
                playground_list[1][1] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "6":
            if playground_list[1][2] == " ":
                playground_list[1][2] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "7":
            if playground_list[2][0] == " ":
                playground_list[2][0] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "8":
            if playground_list[2][1] == " ":
                playground_list[2][1] = player_char
            else:
                print("This box is already filled!")
                player_plays()
        elif player_box == "9":
            if playground_list[2][2] == " ":
                playground_list[2][2] = player_char
            else:
                print("This box is already filled!")
                player_plays()


def computer_plays(level):
    def last_box_check(sequence, char):
        chars_found = 0
        empty_box = None
        for box in sequence:
            if playground_list[box[0]][box[1]] == char:
                chars_found += 1
            elif playground_list[box[0]][box[1]] == " ":
                empty_box = box

        if chars_found == 2 and empty_box is not None:
            return empty_box
        else:
            return None

    def danger(char):
        for i in range(3):
            row_boxes = [(i, j) for j in range(3)]
            the_box = last_box_check(row_boxes, char)
            if the_box is not None:
                return the_box

        for j in range(3):
            col_boxes = [(i, j) for i in range(3)]
            the_box = last_box_check(col_boxes, char)
            if the_box is not None:
                return the_box

        the_box = last_box_check([(0, 0), (1, 1), (2, 2)], char)
        if the_box is not None:
            return the_box

        the_box = last_box_check([(0, 2), (1, 1), (2, 0)], char)
        if the_box is not None:
            return the_box

    if level == "1":
        computer_position_row = randrange(3)
        computer_position_col = randrange(3)
        # MAKE SURE ΟΤΙ ΔΕΝ ΘΑ ΠΑΙΞΟΥΝ ΣΤΗΝ ΙΔΙΑ ΘΕΣΗ ΠΑΙΚΤΗΣ ΚΑΙ ΥΠΟΛΟΓΙΣΤΗΣ

        if playground_list[computer_position_row][computer_position_col] == " ":
            playground_list[computer_position_row][computer_position_col] = computer_char
            print("")
            """
            print("Please wait while the computer is thinking about its next move...")
            input("Press enter to proceed!")
            """
        else:
            computer_plays(level)
    elif level == "2":
        off_box = danger(computer_char)
        the_box = danger(player_char)
        if off_box is not None:
            playground_list[off_box[0]][off_box[1]] = computer_char
        elif the_box is not None:
            playground_list[the_box[0]][the_box[1]] = computer_char
        elif playground_list[1][1] == " ":
            playground_list[1][1] = computer_char
        else:
            corner_boxes = [(0, 0), (0, 2), (2, 0), (2, 2)]
            empty_corner_boxes = []
            for box in corner_boxes:
                if playground_list[box[0]][box[1]] == " ":
                    empty_corner_boxes.append(box)
            if empty_corner_boxes:
                a_box = empty_corner_boxes[randrange(len(empty_corner_boxes))]
                playground_list[a_box[0]][a_box[1]] = computer_char
            else:
                edge_boxes = [(0, 1), (1, 0), (2, 1), (1, 2)]
                empty_edge_boxes = []
                for box in edge_boxes:
                    if playground_list[box[0]][box[1]] == " ":
                        empty_edge_boxes.append(box)
                if empty_edge_boxes:
                    a_box = empty_edge_boxes[randrange(len(empty_edge_boxes))]
                    playground_list[a_box[0]][a_box[1]] = computer_char


def winner_check_tic():
    global j
    # ΟΡΙΖΟΝΤΙΟΙ
    if playground_list[0][0] == playground_list[0][1] and playground_list[0][1] == playground_list[0][2] and \
            playground_list[0][0] != " ":
        if playground_list[0][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[0][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    elif playground_list[1][0] == playground_list[1][1] and playground_list[1][1] == playground_list[1][2] and \
            playground_list[1][0] != " ":
        if playground_list[1][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[1][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    elif playground_list[2][0] == playground_list[2][1] and playground_list[2][1] == playground_list[2][2] and \
            playground_list[2][0] != " ":
        if playground_list[2][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("Player wins!")
            j += 1
        elif playground_list[2][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    # ΚΑΘΕΤΟΙ
    elif playground_list[0][0] == playground_list[1][0] and playground_list[1][0] == playground_list[2][0] and \
            playground_list[0][0] != " ":
        if playground_list[0][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[0][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    elif playground_list[0][1] == playground_list[1][1] and playground_list[1][1] == playground_list[2][1] and \
            playground_list[0][1] != " ":
        if playground_list[0][1] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[0][1] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    elif playground_list[0][2] == playground_list[1][2] and playground_list[1][2] == playground_list[2][2] and \
            playground_list[0][2] != " ":
        if playground_list[0][2] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[0][2] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    # ΔΙΑΓΩΝΙΟΙ
    elif playground_list[0][0] == playground_list[1][1] and playground_list[1][1] == playground_list[2][2] and \
            playground_list[0][0] != " ":
        if playground_list[0][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[0][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1
    elif playground_list[2][0] == playground_list[1][1] and playground_list[1][1] == playground_list[0][2] and \
            playground_list[2][0] != " ":
        if playground_list[2][0] == player_char:
            print_playground()
            print("The game has ended!")
            print("You win!")
            j += 1
        elif playground_list[2][0] == computer_char:
            print("The game has ended!")
            print("Computer wins!")
            j += 1


j = 0
i = 0


def main():
    # MAIN
    global i
    global j
    level = input("Choose level (1-easy, 2-hard): ")
    while True:
        if level == "1" or level == "2":
            break
        else:
            level = input("Choose level (1-easy, 2-hard): ")



    # GAME LOOP
    # ΠΑΙΖΕΙ ΑΥΤΟΣ ΠΟΥ ΝΙΚΗΣΕ ΣΤΟ ROCK - PAPER - SCISSORS
    while True:
        if winner == "player":
            if j == 0 and i < 9:
                player_plays()
                winner_check_tic()
                i += 1
            elif j == 1:
                break
            if j == 0 and i < 9:
                computer_plays(level)
                print_playground()
                winner_check_tic()
                i += 1
            elif j == 1:
                break
        elif winner == "computer":
            if j == 0 and i < 9:
                computer_plays(level)
                print_playground()
                winner_check_tic()
                i += 1
            elif j == 1:
                break
            if j == 0 and i < 9:
                player_plays()
                print_playground()
                winner_check_tic()
                i += 1
            elif j == 1:
                break

        if i == 9 and j == 0:
            print("It's a tie!")
            break


print_playground_ref()
print("=" * 17)

# ROCK - PAPER - SCISSORS
winner = None
choices = ["rock", "paper", "scissors"]
while winner is None:
    computer_choice = choices[randrange(3)]
    """ FOR TESTING PURPOSES """
    print(computer_choice)
    player_choice = input("Rock, paper or scissors? write here: ").lower().strip()
    winner_check(player_choice, computer_choice)

# PLAYER CHOOSES CHARACTER
player_char = input("Please choose your character (X or O): ").upper().strip()
while True:
    if player_char.isalpha():
        # ACCEPT GREEK VALUES
        if player_char == "Χ":
            player_char = "X"
        elif player_char == "Ο":
            player_char = "O"
        while player_char != "X" and player_char != "O":
            print("Please enter only X or O!")
            player_char = input("Please choose your character (X or O): ").upper().strip()
        break
    else:
        print("Please enter a valid entry!")
        player_char = input("Please choose your character (X or O): ").upper().strip()
computer_char = 0
if player_char == "X":
    computer_char = "O"
else:
    computer_char = "X"

main()

print("")
print("Thank you for playing!", end="")
input(" Press ENTER to quit..")
