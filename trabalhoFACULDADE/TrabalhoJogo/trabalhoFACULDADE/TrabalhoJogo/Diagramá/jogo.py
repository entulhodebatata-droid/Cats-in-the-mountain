import pygame

from Diagramá.Const import WIN_WIDTH, WIN_HEIGHT
from Diagramá.interface import interface


class jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def Run(self, ):

        while True:
            Interface = interface(self.window)
            Interface.run()
            pass
