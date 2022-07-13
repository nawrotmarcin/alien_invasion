import pygame


class BackGround():

	def __init__(self, screen):
		self.screen = screen

		self.bg_image = pygame.image.load('resources/bq_image.png')
		self.rect = self.bg_image.get_rect()
		self.screen_rect = screen.get_rect()

	def blitme(self):
		"""Wyświetlanie wyśrodkowanego tła"""
		self.screen.blit(self.bg_image, self.rect)
