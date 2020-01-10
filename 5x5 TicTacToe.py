#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:08:59 2020

@author: rishi
"""

# --------- Global Variables -----------

# Will hold our game board data
board = ["-" for i in range(1,26)]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"

#List of values to select in our 5 x 5 game
values = [str(i) for i in range(1, 26)]

# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4]  + "     1 | 2 | 3 | 4 | 5")
  print(board[5] + " | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9]  + "     6 | 7 | 8 | 9 | 10")
  print(board[10] + " | " + board[11] + " | " + board[12] +" | " + board[13] + " | " + board[14]  + "    11 |12 |13 |14 | 15")
  print(board[15] + " | " + board[16] + " | " + board[17] +" | " + board[18] + " | " + board[19]  + "    16 |17 |18 |19 | 20")
  print(board[20] + " | " + board[21] + " | " + board[22] +" | " + board[23] + " | " + board[24]  + "    21 |22 |23 |24 | 25")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-25: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in values:
      position = input("Choose a position from 1-25: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] == board[3] == board[4] != "-"
  row_2 = board[5] == board[6] == board[7] == board[8] == board[9] != "-"
  row_3 = board[10] == board[11] == board[12] == board[13] == board[14] != "-"
  row_4 = board[15] == board[16] == board[17] == board[18] == board[19] != "-"
  row_5 = board[20] == board[21] == board[22] == board[23] == board[24] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3 or row_4 or row_5:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[5] 
  elif row_3:
    return board[10] 
  elif row_4:
    return board[15]
  elif row_4:
    return board[20]
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[5] == board[10] == board[15] == board[20] != "-"
  column_2 = board[1] == board[6] == board[11] == board[16] == board[21] != "-"
  column_3 = board[2] == board[7] == board[12] == board[17] == board[22] != "-"
  column_4 = board[3] == board[8] == board[13] == board[18] == board[23] != "-"
  column_5 = board[4] == board[9] == board[14] == board[19] == board[24] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3 or column_4 or column_5:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2]
  elif column_4:
    return board[3]
  elif column_5:
    return board[4] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[6] == board[12] == board[18] == board[24] != "-"
  diagonal_2 = board[4] == board[8] == board[12] == board[16] == board[20] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[4]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()