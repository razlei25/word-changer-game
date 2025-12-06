def is_valid_change(word1, word2):
   """Check if word2 differs from word1 by only one letter."""
   if len(word1) != len(word2):
       return False
   return sum(1 for a, b in zip(word1, word2) if a != b) == 1


class WordLadderGame:
    def __init__(self, word_length, start_word, goal_word):
        self.word_length = word_length
        self.start_word = start_word.lower().strip()
        self.goal_word = goal_word.lower().strip()
        self.current_word = self.start_word
        self.moves = [self.start_word]

    def validate_word(self, word):
        word = word.lower().strip()
        if not isinstance(word, str) or not word:
            return False, "Words must be strings."
        if not word.isalpha():
            return False, "Words must contain only letters."
        if len(word) != self.word_length:
            return False, f"Word must be exactly {self.word_length} letters."
        return True, ""

    def validate_start_and_goal(self):
        valid_start, msg_start = self.validate_word(self.start_word)
        valid_goal, msg_goal = self.validate_word(self.goal_word)
        if not valid_start:
            return False, f"Start word error: {msg_start}"
        if not valid_goal:
            return False, f"Goal word error: {msg_goal}"
        if self.start_word == self.goal_word:
            return False, "Goal word must be different from the start word."
        return True, ""

    def make_move(self, new_word):
        new_word = new_word.lower().strip()
        valid, msg = self.validate_word(new_word)
        if not valid:
            return False, msg
        if not is_valid_change(self.current_word, new_word):
            return False, "Invalid move! Your word must change exactly one letter."
        self.current_word = new_word
        self.moves.append(new_word)
        return True, ""

    def is_finished(self):
        return self.current_word == self.goal_word

    def get_state(self):
        return {
            'current_word': self.current_word,
            'goal_word': self.goal_word,
            'moves': self.moves.copy(),
            'finished': self.is_finished()
        }