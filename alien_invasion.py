import sys

import pygame


def run_game():
	# Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Inwazja obcych")

	# Rozpoczęcie pętli głównej gry
	while True:

		# Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Wyśwetlanie ostatnio zmodyfikowanego ekranu.
		pygame.display.flip()


run_game()
