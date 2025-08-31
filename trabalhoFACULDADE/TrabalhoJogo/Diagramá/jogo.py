import pygame

from Diagramá.Const import WIN_WIDTH, WIN_HEIGHT, INTERFACE
from Diagramá.Pontos import Pontos
from Diagramá.interface import interface
from Diagramá.niveis import niveis


class jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def Run(self, ):

        while True:
            score = Pontos(self.window)
            Interface = interface(self.window)
            return_menu = Interface.run()

            if return_menu in [INTERFACE[0], INTERFACE[1], INTERFACE[2]]:
                pontos_jogador = [0, 0]
                level = niveis(self.window, 'fundo1', return_menu, pontos_jogador)
                return_level = level.run(pontos_jogador)
                if return_level:
                    level = niveis(self.window, 'fundo2', return_menu, pontos_jogador)
                    return_level = level.run(pontos_jogador)
                    if return_level:
                        score.save(return_level, pontos_jogador)

            elif return_menu == INTERFACE[3]:
                score.show()
            elif return_menu == INTERFACE[4]:
                pygame.quit()
                quit()
            else:
                pass
