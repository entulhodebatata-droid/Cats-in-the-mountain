import pygame

from Diagramá.Const import WIN_WIDTH, WIN_HEIGHT, INTERFACE
from Diagramá.interface import interface
from Diagramá.niveis import niveis


class jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def Run(self, ):

        while True:
            Interface = interface(self.window)
            retorno = Interface.run()

            if retorno in [INTERFACE[0], INTERFACE[1], INTERFACE[2]]:
                level = niveis(self.window, 'fase1', retorno)
                retorno = level.run()
            elif retorno == INTERFACE[4]:
                pygame.quit()
                quit()
            else:
                pass
