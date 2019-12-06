import pygame
import random
import time


pygame.init()
pygame.font.init()
pygame.display.set_caption('Snake Game')
window_width = 440
window_height = 480
clock = pygame.time.Clock()
player = []

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
	myfont = pygame.font.SysFont('Segoe UI', 40)
	# myfont_bold = pygame.font.Font('Segoe UI', 20, True)
	text_score = myfont.render('SCORE: ', True, (0, 0, 0))
	text_score_number = myfont.render(str(game.score), True, (0, 0, 0))
	game.screen.blit(text_score, (5, window_height-30))
	game.screen.blit(text_score_number, (120, window_height-30))
	game.screen.blit(game.background_image, [10, 10])
	game.screen.blit(food.image, (food.x, food.y))
	for i in reversed(range(1,len(player))):
		player[i].update(player[i-1].x, player[i-1].y)
		game.screen.blit(player[i].image, (player[i].x, player[i].y))
	player[0].move(food)
	player[0].update(player[0].x, player[0].y)
	game.screen.blit(player[0].image, (player[0].x, player[0].y))
	pygame.display.update()
	
def event_handler(events):
	for event in events:
		try:
			if event.key == pygame.K_UP:
				player[0].direction = 1
			elif event.key == pygame.K_DOWN:
				player[0].direction = 2
			elif event.key == pygame.K_LEFT:
				player[0].direction = 3
			elif event.key == pygame.K_RIGHT:
				player[0].direction = 4
		except:
			pass
game = Game(window_width, window_height)
player.append(Player(game, 0.5 * game.window_width, 0.5 * game.window_height))
food = Food(game)
run = True
while game.game_over == False:
	events = pygame.event.get()
	event_handler(events)
	update_screen()
	clock.tick(10)

