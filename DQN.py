from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import random

class DQNAgent:
	def __init__():
		self.reward = 0
		self.gamma = 0.9
		self.learning_rate = 0.0005
		self.model = self.network()

	def check(self, game, player, x, y):
		# going out of border
		if x < 22 or y < 20 or x > game.window_width - 60 or y > game.window_height - 82:
			return 1
		for p in player:
			if p.x == x and p.y == y:
				return 1
		return 0

	def get_state(self, game, player, food):
		state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		# danger up
		x, y = player[0].x + 20, player[0].y
		state[0] = self.check(game, player, x, y)
		# danger down
		x, y = player[0].x - 20, player[0].y
		state[1] = self.check(game, player, x, y)
		# danger left
		x, y = player[0].x, player[0].y - 20
		state[2] = self.check(game, player, x, y)
		# danger right
		x, y = player[0].x, player[0].y + 20
		state[3] = self.check(game, player, x, y)
		#moving up
		state[4] = (player[0].direction == 1) 
		#moving down
		state[5] = (player[0].direction == 2) 
		#moving left
		state[6] = (player[0].direction == 3) 
		#moving right
		state[7] = (player[0].direction == 4) 
		#food on player's left
		state[8] = (food.x < player[0].x)	
		#food on player's right
		state[9] = (food.x > player[0].x)	
		#food below player
		state[10] = (food.y > player[0].y)	
		#food above player
		state[11] = (food.y < player[0].y)
		return state	

	def set_reward(self, game):
		if game.game_over:
			self.reward = -10
		elif game.increase_length:
			self.reward = 10

	def network(self):
		model = Sequential()
        model.add(Dense(output_dim=120, activation='relu', input_dim=12))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=3, activation='softmax'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)
        return model