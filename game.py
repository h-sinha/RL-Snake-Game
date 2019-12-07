from keras.utils import to_categorical
import pygame
import random
import time
from DQN import DQNAgent
import numpy as np

pygame.init()
pygame.font.init()
pygame.display.set_caption('Snake Game')
window_width = 440
window_height = 480
clock = pygame.time.Clock()
max_score = 0
agent = DQNAgent()

class Game:
	def __init__(self, window_width, window_height):
		self.window_width = 440
		self.window_height = 480
		self.screen = pygame.display.set_mode((window_width, window_height))
		self.background_image = pygame.image.load("images/background.png")
		self.score = 0
		self.increase_length = False
		self.game_over = False

class Player:
	def __init__(self, game, x, y, direction = 4):
		self.x = x
		self.y = y
		self.food = 1
		self.eaten = False
		self.image = pygame.image.load('images/snake.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
		self.delta = 20
		self.delta_x = self.delta
		self.delta_y = 0
		# up = 1, down = 2, left = 3, right = 4
		self.direction = direction
	# detect collistion between player head and food
	def detect_collision(self, food):
		if (self.x < food.x + food.width and \
			self.x + self.width > food.x and \
			 self.y < food.y + food.height and \
			 self.y + self.height > food.y):
			game.score += 1
			game.increase_length = True
			food.update()
	def move(self, food):
		self.detect_collision(food);
		if self.direction == 1:
			self.delta_x = 0
			self.delta_y = -self.delta
		elif self.direction == 2:
			self.delta_x = 0
			self.delta_y = self.delta
		elif self.direction == 3:
			self.delta_x = -self.delta
			self.delta_y = 0
		elif self.direction == 4:
			self.delta_x = self.delta
			self.delta_y = 0
		self.x += self.delta_x
		self.y += self.delta_y
		if self.x < 22 or self.y < 20 or self.x > game.window_width - 60 or self.y > game.window_height - 82:
			game.game_over = True

	def update(self, x, y):
		self.x = x
		self.y = y
		
class Food(pygame.sprite.Sprite):
	def __init__(self, game):
		super().__init__()
		self.x = random.randint(20, game.window_width-40)
		self.y = random.randint(20, game.window_height-80)
		self.image = pygame.image.load('images/food.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
	def update(self):
		self.x = random.randint(20, window_width-40)
		self.y = random.randint(20, window_height-80)
def update_screen():
	global max_score
	# increase snake's length on increase in score
	if game.increase_length:
		if player[-1].direction == 1:
			diffx, diffy = 0, -20
		elif player[-1].direction == 2:
			diffx, diffy = 0, 20
		elif player[-1].direction == 3:
			diffx, diffy = 20, 0
		elif player[-1].direction == 4:
			diffx, diffy = -20, 0
		player.append(Player(game, player[-1].x+diffx, player[-1].y+diffy, player[-1].direction))
		game.increase_length = False
	game.screen.fill((255, 255, 255))

	# render score
	myfont = pygame.font.SysFont('Segoe UI', 20)
	max_score = max(max_score, game.score)
	text_score = myfont.render('SCORE: ', True, (0, 0, 0))
	text_score_number = myfont.render(str(game.score), True, (0, 0, 0))
	max_score_render = myfont.render('MAX SCORE: ', True, (0, 0, 0))
	max_score_number = myfont.render(str(max_score), True, (0, 0, 0))
	game.screen.blit(text_score, (5, window_height-30))
	game.screen.blit(text_score_number, (80, window_height-30))
	game.screen.blit(max_score_render, (160, window_height-30))
	game.screen.blit(max_score_number, (300, window_height-30))
	game.screen.blit(game.background_image, [10, 10])
	game.screen.blit(food.image, (food.x, food.y))
	
	# update player position
	for i in reversed(range(1,len(player))):
		player[i].update(player[i-1].x, player[i-1].y)
		game.screen.blit(player[i].image, (player[i].x, player[i].y))
	player[0].move(food)
	player[0].update(player[0].x, player[0].y)
	for i in range(1,len(player)):
		if player[i].x == player[0].x and player[i].y == player[0].y:
			game.game_over = True
	game.screen.blit(player[0].image, (player[0].x, player[0].y))
	pygame.display.update()
	
def event_handler(player, direction):
	if direction == 0:
		return
	player[0].direction = direction

def init(agent, game, player, food):
	state_init1 = agent.get_state(game, player, food)  
	action = [0, 0, 0, 0, 1]
	event_handler(player, np.argmax(np.array(action)))
	state_init2 = agent.get_state(game, player, food)
	reward = agent.set_reward(game)
	agent.memoize(state_init1, action, reward, state_init2, game)
	agent.replay_new(agent.memory)

num_games = 0
while num_games < 1:
	if num_games > 0:
		init(agent, game, player, food)
	num_games += 1
	player = []
	game = Game(window_width, window_height)
	player.append(Player(game, 0.5 * game.window_width, 0.5 * game.window_height))
	food = Food(game)
	while game.game_over == False:
		# for random moves
		agent.epsilon = 80 - num_games
		old_state = agent.get_state(game, player, food)

		if random.randint(0, 200) < agent.epsilon:
			new_direction = to_categorical(random.randint(0, 2), num_classes=5)
		else:
			predict = agent.model.predict(old_state.reshape((1,12)))
			new_direction = to_categorical(np.argmax(predict[0]), num_classes=5)
             
		# perform move  
		event_handler(player, np.argmax(np.array(new_direction)))
		new_state = agent.get_state(game, player, food)
        
		reward = agent.set_reward(game)
		agent.train_model(old_state, new_direction, reward, new_state, game.game_over)

		update_screen()
		clock.tick(60)
		time.sleep(3)

	agent.replay_new(agent.memory)
	print('Game', num_games, '      Score:', game.score)
	agent.model.save_weights('weights.hdf5')

