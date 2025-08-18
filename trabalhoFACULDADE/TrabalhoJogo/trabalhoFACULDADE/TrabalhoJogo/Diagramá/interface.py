#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import srt
from pygame import Surface, Rect
from pygame.font import Font

from Diagramá.Const import WIN_WIDTH, COR_VERDE, COR_PRETO, INTERFACE, COR_ROXA


class interface:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load ('./assets/capa.png')
        self.rect = self.surf.get_rect(left= 0, top= 0)

    def run(self, ):
        pygame.mixer_music.load('./assets/interface.mp3')
        pygame.mixer_music.play(-1)
        while True:
           self.window.blit(source=self.surf, dest=self.rect)

           self.interface_text(20, 'Criação de goiaba', COR_PRETO, ((WIN_WIDTH / 2), 40))

           for i in range(len(INTERFACE)):
               self.interface_text(52, INTERFACE[i], COR_PRETO, ((WIN_WIDTH / 2), 200 + 60 * i))
               self.interface_text(50, INTERFACE[i], COR_ROXA, ((WIN_WIDTH / 2), 200 + 60 * i))




           pygame.display.flip()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()

    def interface_text(self, text_size: int, text: srt, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Elephant', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)




