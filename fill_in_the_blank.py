EASY_MAD_LIB = """a cat in the (__1__)"""
EASY_ANSWER = "hat"

MEDIUM_MAD_LIB = """green eggs and (__1__)"""
MEDIUM_ANSWER = "ham"

HARD_MAD_LIB = "how the (__1__) stole christmas"
HARD_ANSWER = "grinch"

def valid_game_difficulty(diff):
	if diff == 'easy' or diff == 'medium' or diff == 'hard':
		return True
	else:
		return False

def select_game_difficulty():
	"""Prompts user to select a difficulty level, repeats until the user chooses a valid response
	Function returns a string: either 'easy' , 'medium', or 'hard'."""
	difficulty = input("Please select a game difficulty by typing it in!\nValid responses are easy, medium, and hard.\n").lower()
	if valid(difficulty):
		return difficulty
	else:
		select_game_difficulty()

def number_of_attempts(diff):
	if diff == 'easy':
		return 3
	elif diff == 'medium':
		return 2
	else:
		return 1

def display_mad_lib(diff, guesses, total_allowed_attempts)