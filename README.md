# Othello AI Game

This project implements an Othello game with AI players using Python. The game can be played through a graphical interface, and the AI players use strategies such as minimax with heuristics to make decisions.

## Features

- **GUI**: Play Othello with a clean graphical interface.
- **AI Players**:
  - `Group1.py`: A custom minimax algorithm with alpha-beta pruning and a custom heuristic for strategic moves.
  - `randy_ai.py`: A custom min AI that selects random moves.

  Other baseline AIs provided to test against the custom AI:
  - `itDeep.py`: An iterative deepening AI with alpha-beta pruning and a heuristic that prioritizes board positions.
  - `noHeur.py`: A minimax AI with alpha-beta pruning but no heuristic, relying solely on piece count.
- **Customizable Matchups**: Configure matches between different AI strategies or play against a human player.

## Requirements

- Python 3.x
- Required libraries: `tkinter` (pre-installed with most Python distributions)

## How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hibaa8/othello-with-AI.git
   cd othello-with-AI
    ```
2. **Run the game with the GUI**:
   ```bash
    python othello_gui.py Group1.py randy_ai.py
   ```
Replace Group1.py and randy_ai.py with any AI scripts you want to match up.

## Files

- **`othello_gui.py`**: GUI implementation for the Othello game.
- **`othello_game.py`**: Core game logic and AI integration.
- **`othello_shared.py`**: Shared utility functions for the game.

### AI Scripts
- **`Group1.py`**: AI using minimax with alpha-beta pruning and a heuristic.
- **`randy_ai.py`**: Baseline random-move AI.
- **`itDeep.py`**: Iterative deepening AI with alpha-beta pruning and a heuristic.
- **`noHeur.py`**: Minimax AI with alpha-beta pruning and no heuristic.

## AI Player Descriptions

### `Group1.py` (created by our group)
- **Strategy**: Implements minimax with alpha-beta pruning and a custom heuristic that prioritizes corners and sides while avoiding positions near corners.
- **Strengths**: Efficient search with deeper lookahead due to alpha-beta pruning; strategic move selection.

### `randy_ai.py`
- **Strategy**: Selects moves randomly from available options.
- **Strengths**: Provides a baseline for testing; easy to beat, useful for benchmarking.

### `itDeep.py`
- **Strategy**: Uses iterative deepening with alpha-beta pruning and heuristics similar to `Group1.py`.
- **Strengths**: Balances time constraints with deeper search; adjusts depth dynamically based on available time.

### `noHeur.py`
- **Strategy**: Implements minimax with alpha-beta pruning without additional heuristics, relying solely on piece count.
- **Strengths**: Simple evaluation function; useful for understanding the impact of heuristics.

## Notes

###  Player Colors
- The **first AI script** (e.g., `Group1.py`) plays as **Black** and moves first.
- The **second AI script** (e.g., `randy_ai.py`) plays as **White** and moves second.

### Troubleshooting
- Ensure all scripts have the correct permissions.
- If the GUI doesn't display or the game doesn't start, check for any errors in the console and verify that all required libraries are installed.

### Acknowledgements
Project completed with Max Watsky and Stephanie P.

Project template forked from https://github.com/daniel-bauer/shape-s20-othello
   
