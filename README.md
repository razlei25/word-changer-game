# Assignment 6 processes

## Program
**Word Changer Game** is a game in which the user inputs two words of the same length and in each turn changes one letter in the first word in order to eventually get to the other word.

Run the program in `word_changer_game_GUI.py`

## Operation
- Dependencies: None other than Python standard libraries.
- System: I am using Python 3.8 on Windows
- Tests: `python -m unittest day05.tests #from root`

## Background
This project is an improved version of the word changer game from assignment 5 in the Basic Programming (Python) course.
The user interaction is through a GUI instead of theough the command line.
Additionally, at the end of each game the user has an option to save the the results to a file to keep track.

## AI prompts (Visual Studio Code copilot GPT-4.1)
- "Create a GUI for the program in word_changer_game.py so that word_changer_game.py would only have the "business logic" of the program (without the interaction part using the input() functions or any other interaction) and another file, named word_changer_game_GUI.py would be run to interact with the game using a GUI."
- "Great. Now I want to add an option for the user at the end of the game to save the results to a .txt file. At the end of the game, the user will be propted with a question to save the game results. If they choose to save the results, all the user to choose where to save the .txt for and under what name (default: "word_changer_game_results.txt" at Downloads). The .txt. file will include 4 lines: "Word changer game results", "Start word: {}", "Goal word: {}", "Number of turns: {}""