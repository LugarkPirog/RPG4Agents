import pygame
import os
import sys


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath('.'))

from player.players import Player
from settings import DEBUG


class Display:
    def __init__(self, player, fps=60):
        self.p = player
        self.srf = pygame.display.set_mode((500,500))
        self._rect = pygame.rect.Rect(250,250, 50,50)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.done = False

    def draw(self):
        """
        draw one frame
        :return:
        """

        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        self.process_events(events)
        self.process_keys(keys)

        self.srf.fill(0)
        pygame.draw.rect(self.srf, (255, 128, 70), self._rect)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def process_keys(self, keys):
        """

        :param keys:
        :return:
        """
        x = 0
        y = 0
        if keys[pygame.K_a]:
            self.p.move('w')
            x += -1
        if keys[pygame.K_d]:
            self.p.move('e')
            x += 1
        if keys[pygame.K_w]:
            self.p.move('n')
            y += -1
        if keys[pygame.K_s]:
            self.p.move('s')
            y += 1
        if keys[pygame.K_q]:
            self.p.quit()
            self.done = True

        self._rect = self._rect.move(x, y)

    def process_events(self, events):
        """

        :param events:
        :return:
        """
        pass

    def start(self):
        """
        main loop
        :return: None
        """
        while not self.done:
            self.draw()


if __name__ == '__main__':
    p = Player('vas', 'warrior', [100, 100])
    d = Display(p)
    d.start()
