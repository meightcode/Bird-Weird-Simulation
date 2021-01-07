import pygame, random, sys, math, time

W=1920
H=1070
screen = pygame.display.set_mode((W,H))
title = pygame.display.set_caption("Simulation")
clock = pygame.time.Clock()
pygame.init()
screen.fill([255,255,255])
pygame.display.flip()

class Game:
	def __init__(self):
		self.bird = []
		for i in range(350):
			self.bird.append(Bird(i))
			self.bird[i].rect.y = random.randint(0,H-30)
			self.bird[i].rect.x = random.randint(0,W-30)
	def birdAppear(self):
		for i in range(len(self.bird)):
			screen.blit(self.bird[i].image, self.bird[i].rect)
	def moveBird(self):
		for i in range(len(self.bird)):
			self.bird[i].move()
	def rotate(self):
		for i in range(len(self.bird)):
			self.bird[i].rotate()
	def checkCollide(self):
		for i in range(len(self.bird)):
			self.bird[i].wallCollide()
	def mouseClick(self,x,y):
		for i in self.bird:
			self.clickEffect(x,y,i)
	def clickEffect(self,x,y,i):
		if x-50 <i.rect.x < x+50 and y-50 < i.rect.y < y+50:
			i.angle -= 180




class Bird(pygame.sprite.Sprite):
	def __init__(self,number):
		super(Bird, self).__init__()
		self.number = number
		self.angle = 0
		self.image = pygame.transform.scale(pygame.image.load('image/cone.png'),(32,32))
		self.rect = self.image.get_rect()
		self.origin_image = pygame.transform.rotozoom(self.image,-90,1)
		self.rect.y = 0
		self.rect.x = 0
	def move(self):
		self.rect.x += math.cos(math.radians(self.angle))*10
		self.rect.y += -math.sin(math.radians(self.angle))*10
	def rotate(self):
		self.angle += random.randint(-5,5)
		self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
		self.rect = self.image.get_rect(center=self.rect.center)
	def wallCollide(self):
		if self.rect.y > H-30:
			self.angle = 90
		elif self.rect.y < 0:
			self.angle = 270
		elif self.rect.x < 0:
			self.angle = 0
		elif self.rect.x > W-30:
			self.angle = 180
		

class BirdRules:
	def __init__(self):
		self.interaction_range = 50
	def checkRange(self):
		for i in range(len(game.bird)):
			for v in range(len(game.bird)):
				if game.bird[i].number != game.bird[v].number:
					if abs(game.bird[i].rect.x - game.bird[v].rect.x)<self.interaction_range and abs(game.bird[i].rect.y - game.bird[v].rect.y)< self.interaction_range:
						if 0 < abs(game.bird[i].angle - game.bird[v].angle) < 90 or 270 < abs(game.bird[i].angle - game.bird[v].angle) < 360:
							game.bird[i].angle = game.bird[v].angle - random.randint(-20,20)
						elif 90 < abs(game.bird[i].angle - game.bird[v].angle) < 180 or 180 < abs(game.bird[i].angle - game.bird[v].angle) < 270:
							game.bird[i].angle+= 50
							game.bird[v].angle+= -50



rules = BirdRules()
game = Game()

running = True
while running:
	start = time.time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			running = False
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN :
			if event.button == 1:
				mx ,my = pygame.mouse.get_pos()
				game.mouseClick(mx, my)

	
	game.birdAppear()
	game.rotate()
	game.checkCollide()
	game.moveBird()
	rules.checkRange()
	end = time.time()

	pygame.display.flip()
	screen.fill([255,255,255])
	


