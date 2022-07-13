import sys

import pygame


def check_events(ship):
	"""Reakcja na zdarzenia generowana przez klawiaturę i myszkę"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				# Przesunięcie statku w prawą stronę
				ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship, bg):
	"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
	# Odświeżenie ekranu w trakcie każdej iteracji pętli.
	# screen.fill(ai_settings.bg_color)
	bg.blitme()
	ship.blitme()

	# Wyśwetlanie ostatnio zmodyfikowanego ekranu.
	pygame.display.flip()
