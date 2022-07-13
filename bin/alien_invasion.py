import pygame

from settings import Settings
from ship import Ship
from background_image import BackGround
import game_functions as gf


def run_game():
	# Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")

	# Utworzenie statku kosmiczego.
	ship = Ship(screen)
	bg = BackGround(screen)

	# Rozpoczęcie pętli głównej gry
	while True:
		gf.check_events(ship)
		gf.update_screen(ai_settings, screen, ship, bg)


run_game()
