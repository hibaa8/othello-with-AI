#!/usr/bin/env python3
# -*- coding: utf-8 -*


import random
import sys
import time
import math

from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    #1 is dark, 2 is light
    opp = 1
    if color == 1:
      opp = 2
    
    return board.count(color) - board.count(opp)


def heuristic(move, board, color):
  #returns a -10 to 25 addifier
  m = 0
  cornerList = [(0,0), (7,0), (0,7), (7,7)]
  aroundCornerList = [(0,1), (1,0), (1,1), (7,1), (6,0), (6,1),(1,7), (0,6), (1,6), (6,6), (7,6), (6,7)]
  sideList = [(0,2),(0,3),(0,4),(0,5),(7,2),(7,3),(7,4),(7,5),(2,0),(3,0),(4,0),(5,0),(2,7),(3,7),(4,7),(5,7)]


  if move in cornerList:
    m = 25
  elif move in aroundCornerList:
    m = -10
  elif move in sideList:
    m = 10

  return m



############ MINIMAX ###############################
#note: implement depth
def minimax_max_node(board, color, depth, alpha, beta):
    opp = 1
    if color == 1:
      opp = 2
      
    moves = get_possible_moves(board, color)
    if len(moves) == 0 or depth == 0:
      return None, compute_utility(board, color)

    maxMove = moves[0]
    maxUti = -math.inf
   
    for i in moves:
      nBoard = play_move(board, color, i[0], i[1])
      move, uti = minimax_min_node(nBoard, color, depth - 1, alpha, beta)
      uti = uti + heuristic(i, board, color)
      if uti > maxUti:
        maxUti = uti
        maxMove = i
      alpha = max(alpha, uti)
      if beta <= alpha:
        break


    return maxMove, maxUti


def minimax_min_node(board, color, depth, alpha, beta):
    
    opp = 1
    if color == 1:
      opp = 2 
    moves = get_possible_moves(board, opp)
    if len(moves) == 0 or depth == 0:
      return None, compute_utility(board, color)

    minMove = moves[0]
    minUti = math.inf
    for i in moves:
      nBoard = play_move(board, opp, i[0], i[1])
      move, uti = minimax_max_node(nBoard, color, depth - 1, alpha, beta)
      uti = uti - heuristic(i, board, opp)
      if uti < minUti:
        minUti = uti
        minMove = i
      beta = min(beta, uti)
      if beta <= alpha:
        break

    
    return minMove, minUti
    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """

    
    bestMoves = []
    times = []

    depth = 1
    contin = True
    origTime = time.time()

    while contin:
      move, uti = minimax_max_node(board, color, depth, -math.inf, math.inf)
      bestMoves.append(move)
      depth += 1
      times.append(time.time() - origTime)
      origTime = time.time()
      if len(times) > 1:
        if sum(times) + (times[-1]/times[-2] * times[-1]) > 4:
          contin = False

    return bestMoves[-2]




####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("VERITDEEP") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
