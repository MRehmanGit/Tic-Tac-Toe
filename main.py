from random import randrange

#Initializing the Tic Tac Toe board as a 2D list
board = [ [ 1 , 2 , 3 ],
          [ 4 , 5 , 6 ],
          [ 7 , 8 , 9 ]]


def display_board(board):
  #Displays the Tic Tac Toe board with current moves
    print(" +---+--------+--------+")
    for rows in board:
        for ind in rows:
            print(" " ,ind ,end="  |   ")
        print()
        print(" +---+--------+--------+")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    counter  = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if index != "X" or index == "O":
                tup = (counter, index_counter)
                free_fields.append(tup)
                index_counter += 1
            else:
                index_counter += 1
                continue
        index_counter = 0
        counter+=1
    return free_fields


def number_to_column_locator(num):
# Converts a numeric input representing a position on the Tic Tac Toe board into board coordinates (row, column).
    counter = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if board[counter][index_counter] == num:
                tup = (counter, index_counter)
                return tup
            index_counter+=1

        index_counter = 0
        counter+=1


def enter_move(board):
#The function draws the users move and updates the board.
    flag = True
    while flag:
        user_input = int(input("Enter your move between 1-9: "))
        location = number_to_column_locator(user_input)
        if user_input in range (1,10) and location in make_list_of_free_fields(board):
            board[location[0]][location[1]] = "O"
            flag = False
        else:
            print("Invalid move")
            print("Try again, Enter a number between 1-9: ")


def draw_move(board):
    #The function draws the computer's move and updates the board.

    flag = True
    while flag:
        index_choice_X = randrange(3)
        list_choice_X = randrange(3)
        tuple_of_computer_location = (list_choice_X, index_choice_X)
        if tuple_of_computer_location  in make_list_of_free_fields(board):
            board[tuple_of_computer_location[0]][tuple_of_computer_location[1]] = "X"
            flag = False


def horizontal_check(board):
  # Checks horizontally for a win condition for 'X' or 'O' on the Tic Tac Toe board.
    counter_for_x = 0
    counter_for_y = 0
    row_counter = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if board[row_counter][index_counter] == "X":
                counter_for_x += 1
            elif board[row_counter][index_counter] == "O":
                counter_for_y +=1

            index_counter += 1

        if counter_for_x == 3:
            return 1
        elif counter_for_y == 3:
            return 2
        else:
            counter_for_x = 0
            counter_for_y = 0
            index_counter = 0
            row_counter += 1

  #returns -1 if no horizontial win
    return -1


def vertical_check(board):
  #Checks vertically for a win condition for 'X' or 'O' on the Tic Tac Toe board.
    counter_for_x = 0
    counter_for_y = 0
    row_counter = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if board[index_counter][row_counter] == "X":
                counter_for_x += 1
            elif board[index_counter][row_counter] == "O":
                counter_for_y += 1

            index_counter += 1

        if counter_for_x == 3:
            return 1
        elif counter_for_y == 3:
            return 2
        else:
            counter_for_x = 0
            counter_for_y = 0
            index_counter = 0
            row_counter += 1

    #returns -1 if no horizontial win
    return -1


def diagonal_check(board):
  #Checks diagonally for a win condition for 'X' or 'O' on the Tic Tac Toe board.
    counter_for_x = 0
    counter_for_y = 0
    row_counter = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if row_counter == index_counter:
                if board[row_counter][index_counter] == "X":
                    counter_for_x += 1
                elif board[row_counter][index_counter] == "O":
                    counter_for_y += 1
            index_counter += 1

        index_counter = 0
        row_counter += 1
    #end of loop
    #Condition for Diagonal Win
    if counter_for_x == 3:
        return 1
    elif counter_for_y == 3:
        return 2
    else:
        return -1


def antidiagonal_check(board):
  #Checks diagonally (anti-diagonal) for a win condition for 'X' or 'O' on the Tic Tac Toe board.
    counter_for_x = 0
    counter_for_o = 0
    row_counter = 0
    index_counter = 0
    for rows in board:
        for index in rows:
            if (row_counter + index_counter) == 2:
                if board[row_counter][index_counter] == "X":
                    counter_for_x += 1
                elif board[row_counter][index_counter] == "O":
                    counter_for_o += 1

            index_counter += 1
        index_counter = 0
        row_counter += 1
    #loop ends here
  #Condition for anti-diagonal win
    if counter_for_x == 3:
        return 1
    elif counter_for_o == 3:
        return 2
    else:
        return -1


def victory_for(board):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    final_winner_h = horizontal_check(board)
    final_winner_v = vertical_check(board)
    final_winner_d = diagonal_check(board)
    final_winner_anti = antidiagonal_check(board)


    if final_winner_h == 1:
        print("Computer has won H!")
    elif final_winner_h == 2:
        print("You've won H!")
    else:
        if final_winner_v == 1:
            print("Computer has won V!")
        elif final_winner_v == 2:
            print("You've won V!")
        else:
            if final_winner_d == 1:
                print("Computer has won D!")
            elif final_winner_d == 2:
                print("You've won D!")
            else:
                if final_winner_anti == 1:
                    print("Computer has won A!")
                elif final_winner_anti == 2:
                    print("You've won A!")
                else:
                    return False
    return True


def play(board):
    #This function manages player turns, handles input validation, updates the board,
    #checks for win conditions (horizontal, vertical, diagonal, anti-diagonal),
    #and displays the board after each move. The game continues until a player wins.
  
    display_board(board)

    flag = True
    isWin = False

    for i in range(1,10):
        if flag == True:
            enter_move(board)
            flag = False
        else:
            draw_move(board)
            flag = True

        display_board(board)
        if victory_for(board) == True:
            isWin = True
            break
    if isWin == False:
        print("nobody won")


# Executes the main gameplay loop for Tic Tac Toe.
play(board)
