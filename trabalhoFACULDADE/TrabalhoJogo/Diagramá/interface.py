#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from Diagramá.Const import WIN_WIDTH, COR_VERDE, COR_PRETO, INTERFACE, COR_ROXA


class interface:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/capa.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    # ================================================================== (Música)
    def run(self, ):
        menu = 0
        pygame.mixer_music.load('./assets/interface.mp3')
        pygame.mixer_music.play(-1)
        # ================================================================== (Interface visual)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            for i in range(len(INTERFACE)):

                self.interface_text(50, 'Cats in the', COR_ROXA, ((WIN_WIDTH / 2), 40))
                self.interface_text(40, 'mountain', COR_ROXA, ((WIN_WIDTH / 2), 65))

                if i == menu:
                    self.interface_text(31, INTERFACE[i], COR_PRETO, ((WIN_WIDTH / 2), 140 + 30 * i))
                    self.interface_text(30, INTERFACE[i], COR_VERDE, ((WIN_WIDTH / 2), 140 + 30 * i))
                else:
                    self.interface_text(31, INTERFACE[i], COR_PRETO, ((WIN_WIDTH / 2), 140 + 30 * i))
                    self.interface_text(30, INTERFACE[i], COR_ROXA, ((WIN_WIDTH / 2), 140 + 30 * i))

            # ================================================================== (Menu)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # ==================================================================
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu < len(INTERFACE) - 1:
                            menu += 1
                        else:
                            menu = 0
                    # ==================================================================
                    if event.key == pygame.K_UP:
                        if menu > 0:
                            menu -= 1
                        else:
                            menu = len(INTERFACE) - 1
                    # ==================================================================
                    if event.key == pygame.K_RETURN:
                        return INTERFACE[menu]
            # ==================================================================
            pygame.display.flip()

    def interface_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Elephant', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
