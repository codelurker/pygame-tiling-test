
# This Class represents the human-controllable hero of the game.

import util
from Animation import *


class Hero:
	# TODO user interaction

	(UP_WALK, UP_STAND, DOWN_WALK, DOWN_STAND,
			LEFT_WALK, LEFT_STAND, RIGHT_WALK, RIGHT_STAND) = range(8)


	def __init__(self):
		img = util.load_image('rpg_sprite_walk.png')
		order = range(8)
		delay = 4  # each phase of the animation lasts 6 frames
		offset = (0,0)  # no offset

		self.__walk_down = Animation(order)
		for down_rect in [ (4+i*24, 0, 16, 31) for i in range(8) ]:
			self.__walk_down.add_frame(img, down_rect, delay, offset)

		self.__walk_up = Animation(order)
		for up_rect in [ (4+i*24, 32, 16, 31) for i in range(8) ]:
			self.__walk_up.add_frame(img, up_rect, delay, offset)

		self.__walk_left = Animation(order)
		for left_rect in [ (4+i*24, 64, 16, 31) for i in range(8) ]:
			self.__walk_left.add_frame(img, left_rect, delay, offset)

		self.__walk_right = Animation(order)
		for right_rect in [ (4+i*24, 96, 16, 31) for i in range(8) ]:
			self.__walk_right.add_frame(img, right_rect, delay, offset)

		# initial values
		self.state = self.DOWN_WALK
		self.x = 60
		self.y = 60

	
	def stand(self):
		if self.state == Hero.DOWN_WALK:
			self.state = Hero.DOWN_STAND
		elif self.state == Hero.UP_WALK:
			self.state = Hero.UP_STAND
		elif self.state == Hero.LEFT_WALK:
			self.state = Hero.LEFT_STAND
		elif self.state == Hero.RIGHT_WALK:
			self.state = Hero.RIGHT_STAND


	def tick(self):
		if self.state == Hero.DOWN_WALK:
			self.y += 1
		elif self.state == Hero.UP_WALK:
			self.y -= 1
		elif self.state == Hero.LEFT_WALK:
			self.x -= 1
		elif self.state == Hero.RIGHT_WALK:
			self.x += 1


	def get_bounds(self):
		# TODO!!!
		return (self.x, self.y, self.x+32, self.y+32)


	def show(self, screen):
		pos = (self.x, self.y)

		if self.state == Hero.DOWN_WALK:
			self.__walk_down.show(screen, pos)
		elif self.state == Hero.UP_WALK:
			self.__walk_up.show(screen, pos)
		elif self.state == Hero.LEFT_WALK:
			self.__walk_left.show(screen, pos)
		elif self.state == Hero.RIGHT_WALK:
			self.__walk_right.show(screen, pos)
		elif self.state == Hero.DOWN_WALK:
			screen.blit(img, pos, (4, 0, 16, 31))
		elif self.state == Hero.UP_WALK:
			screen.blit(img, pos, (4, 0, 16, 31))
		elif self.state == Hero.LEFT_WALK:
			screen.blit(img, pos, (4, 0, 16, 31))
		elif self.state == Hero.RIGHT_WALK:
			screen.blit(img, pos, (4, 0, 16, 31))


		# TODO other states

