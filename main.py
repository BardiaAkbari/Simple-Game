import pygame
import sys


class AlienGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Simple Game")
        self.screen.fill((255, 255, 255))
        self.my_ship = Ship(self)

    def run(self):

        while True:
            self._event_handler()
            self.my_ship.update()
            self.render()

    def _event_handler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    self.my_ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.my_ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.my_ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.my_ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.my_ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.my_ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.my_ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.my_ship.moving_down = False

    def render(self):
        self.my_ship.blitme()
        pygame.display.flip()


class Ship:

    def __init__(self, my_ai):
        self.game_screen = my_ai.screen
        self.game_screen_rect = self.game_screen.get_rect()
        self.image = pygame.image.load("D:\\Python\\Programming\\Main\\Simple Game\\Image\\Ship1.bmp")
        self.image_rect = self.image.get_rect()

        self.image_rect.midbottom = self.game_screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        if self.moving_right and self.image_rect.right < self.game_screen_rect.right:
            self.image_rect.x += 1

        if self.moving_left and self.image_rect.left > self.game_screen_rect.left:
            self.image_rect.x -= 1

        if self.moving_up and self.image_rect.top > self.game_screen_rect.top:
            self.image_rect.y -= 1

        if self.moving_down and self.image_rect.bottom < self.game_screen_rect.bottom:
            self.image_rect.y += 1

    def blitme(self):
        self.game_screen.blit(self.image, self.image_rect)


if __name__ == "__main__":
    my_alien_game = AlienGame()
    my_alien_game.run()
