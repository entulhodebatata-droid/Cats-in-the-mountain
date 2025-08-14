import pygame

class jogo:
    def __init__(self):
        self.window = None
    def Run(self, ):

        print("Inicio")
        pygame.init()
        window = pygame.display.set_mode(size=(1400, 700))
        print('fim')

        # ----------------------------------
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        # fechar definitivamente a janela
        # ----------------------------------
