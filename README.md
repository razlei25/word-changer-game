# Assignment 6 processes

## Program
**Word Changer Game** is a game in which the user inputs two words of the same length and in each turn changes one letter in the start word in order to eventually get to the goal word.

Run the program in `word_changer_game_GUI.py`


## Example

![Start of game example](images/Screenshot%202025-12-06%20223126%201.png)

![End of game example](images/Screenshot%202025-12-06%20223043%202.png)


## Operation
- Dependencies: **tkinter**, **unittest** # Both libraries are included with standard Python installations
```python
import tkinter as tk  # For GUI
import unittest       # For testing
```
- System: I am using Python 3.8 on Windows
- Tests: `python -m unittest day05.tests #from root`

## Background
This project is an improved version of the word changer game from assignment 5 in the Basic Programming (Python) course.
The user interaction is through a GUI instead of through the command line.
Additionally, at the end of each game the user has an option to save the the results to a file to keep track.

## AI prompts (Visual Studio Code copilot GPT-4.1)
- "Create a GUI for the program in word_changer_game.py so that word_changer_game.py would only have the "business logic" of the program (without the interaction part using the input() functions or any other interaction) and another file, named word_changer_game_GUI.py would be run to interact with the game using a GUI."
- "Great. Now I want to add an option for the user at the end of the game to save the results to a .txt file. At the end of the game, the user will be propted with a question to save the game results. If they choose to save the results, all the user to choose where to save the .txt for and under what name (default: "word_changer_game_results.txt" at Downloads). The .txt. file will include 4 lines: "Word changer game results", "Start word: {}", "Goal word: {}", "Number of turns: {}""
- "Update the tests for the updated program code (both files, "business logic" and GUI)"
- "Update in pyproject.toml, wherever suitable, the dependencies required to run this program."
- "In the README file, under "Dependencies", explain how to import the libraries"