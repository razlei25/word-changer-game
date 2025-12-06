# To test, run (from root*) in cammand line: python -m unittest day05.tests_word_changer -v
# Alternatively, run this file directly: day05/tests_word_changer.py 
# * Run from project root = python-course-assignments

import unittest
from word_changer_game import is_valid_change, WordLadderGame


class TestWordChanger(unittest.TestCase):
    def test_is_valid_change_cases(self):
        self.assertTrue(is_valid_change("cat", "cot"))
        self.assertFalse(is_valid_change("cat", "cat"))
        self.assertFalse(is_valid_change("cat", "dog"))
        self.assertFalse(is_valid_change("cat", "cats"))
        self.assertFalse(is_valid_change("", "a"))

    def test_word_ladder_game_flow(self):
        game = WordLadderGame(3, "cat", "dog")
        valid, msg = game.validate_start_and_goal()
        self.assertTrue(valid)
        self.assertFalse(game.is_finished())
        # Move 1: cat -> cot
        success, msg = game.make_move("cot")
        self.assertTrue(success)
        self.assertFalse(game.is_finished())
        # Move 2: cot -> dot
        success, msg = game.make_move("dot")
        self.assertTrue(success)
        self.assertFalse(game.is_finished())
        # Move 3: dot -> dog
        success, msg = game.make_move("dog")
        self.assertTrue(success)
        self.assertTrue(game.is_finished())
        state = game.get_state()
        self.assertEqual(state['moves'], ["cat", "cot", "dot", "dog"])
        self.assertEqual(state['goal_word'], "dog")
        self.assertEqual(state['current_word'], "dog")
        self.assertTrue(state['finished'])

    def test_invalid_moves(self):
        game = WordLadderGame(3, "cat", "dog")
        # Invalid move: wrong length
        success, msg = game.make_move("cats")
        self.assertFalse(success)
        # Invalid move: not a word
        success, msg = game.make_move("123")
        self.assertFalse(success)
        # Invalid move: not one letter change
        success, msg = game.make_move("dog")
        self.assertFalse(success)

    def test_invalid_start_and_goal(self):
        # Same start and goal
        game = WordLadderGame(3, "cat", "cat")
        valid, msg = game.validate_start_and_goal()
        self.assertFalse(valid)
        # Invalid start word
        game = WordLadderGame(3, "c@t", "dog")
        valid, msg = game.validate_start_and_goal()
        self.assertFalse(valid)
        # Invalid goal word
        game = WordLadderGame(3, "cat", "d0g")
        valid, msg = game.validate_start_and_goal()
        self.assertFalse(valid)

    def test_gui_launch(self):
        # Basic test to ensure GUI can be created (does not test interaction)
        import sys
        if "pytest" in sys.modules:
            return  # skip for pytest environments
        try:
            import tkinter as tk
            from word_changer_game_GUI import WordLadderGUI
            root = tk.Tk()
            app = WordLadderGUI(root)
            root.destroy()
        except Exception as e:
            self.fail(f"GUI failed to launch: {e}")


if __name__ == "__main__":
    unittest.main()
