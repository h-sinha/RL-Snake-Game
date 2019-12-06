import pygame
import random
import time


pygame.init()
pygame.font.init()
pygame.display.set_caption('Snake Game')
window_width = 440
window_height = 460
clock = pygame.time.Clock()

class Game:
	def __init__(self, window_width, window_height):
		self.window_width = 440
		self.window_height = 480
		self.screen = pygame.display.set_mode((window_width, window_height))
		self.background_image = pygame.image.load("images/background.png")
		self.score = 0

class Player():
	def __init__(self, game):
		self.x = 0.5 * game.window_width
		self.y = 0.5 * game.window_height
		self.position = []
		self.position.append([self.x, self.y])
		self.food = 1
		self.eaten = False
		self.image = pygame.image.load('images/snake.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
		self.delta = 2
		self.delta_x = self.delta
		self.delta_y = 0
		# up = 1, down = 2, left = 3, right = 4
		self.direction = 4
	def move(self, direction):
		if direction == 1:
			self.delta_x = 0
			self.delta_y = -self.delta
		elif direction == 2:
			self.delta_x = 0
			self.delta_y = self.delta
		elif direction == 3:
			self.delta_x = -self.delta
			self.delta_y = 0
		elif direction == 4:
			self.delta_x = self.delta
			self.delta_y = 0
	def detect_collision(self, food):
		if (self.x < food.x + food.width and \
			self.x + self.width > food.x and \
			 self.y < food.y + food.height and \
			 self.y + self.height > food.y):
			game.score += 1
			food.update()
	def update(self, food):
		self.detect_collision(food);
		self.x += self.delta_x
		self.y += self.delta_y

class Food(pygame.sprite.Sprite):
	def __init__(self, game):
		super().__init__()
		self.x = random.randint(30, game.window_width-40)
		self.y = random.randint(60, game.window_height-60)
		self.image = pygame.image.load('images/food.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
	def update(self):
		self.x = random.randint(30, window_width-40)
		self.y = random.randint(60, window_height-60)

def update_screen():
	player.update(food)
	game.screen.fill((255, 255, 255))
	game.screen.blit(game.background_image, [10, 10])
	game.screen.blit(food.image, (food.x, food.y))
	game.screen.blit(player.image, (player.x, player.y))
	pygame.display.update()
	
def event_handler(events):
	for event in events:
		try:
			if event.key == pygame.K_UP:
				player.move(1)
			elif event.key == pygame.K_DOWN:
				player.move(2)
			elif event.key == pygame.K_LEFT:
				player.move(3)
			elif event.key == pygame.K_RIGHT:
				player.move(4)
		except:
			pass
game = Game(window_width, window_height)
player = Player(game)
food = Food(game)
run = True
while run:
	events = pygame.event.get()
	event_handler(events)
	update_screen()
	clock.tick(60)

