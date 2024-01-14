def rpsWinner(player1, player2):

	if 'rock' in player1:

		if 'rock' in player2:
			return 'tie'
		elif 'paper' in player2:
			return 'player two'
		elif 'scissors' in player2:
			return 'player one'
		else:
			return 'invalid input'

	elif 'paper' in player1:

		if 'rock' in player2:
			return 'player one'
		elif 'paper' in player2:
			return 'tie'
		elif 'scissors' in player2:
			return 'player two'
		else:
			return 'invalid input'

	elif 'scissors' in player1:

		if 'rock' in player2:
			return 'player two'
		elif 'paper' in player2:
			return 'player one'
		elif 'scissors' in player2:
			return 'tie'
		else:
			return 'invalid input'

	else:
		return 'invalid input'


assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'