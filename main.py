import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	time = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	player = Player(x, y)

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)

		for obj in asteroids:
			if obj.collision_check(player):
				print("Game over!")
				sys.exit()

		screen.fill((0,0,0))

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		dt = time.tick(60) / 1000

if __name__ == "__main__":
	main()