#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Diagramá.Const import VELOCIDADE, WIN_HEIGHT, WIN_WIDTH, JOGADOR_KEYUP, JOGADOR_KEYDOWN, JOGADOR_KEYLEFT, \
    JOGADOR_KEYRIGHT, JOGADOR_TIRO, DELAY_TIRO
from Diagramá.entity import entity
from Diagramá.tirojogador import tirojogador


class jogador(entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.delay_tiro = DELAY_TIRO[self.name]

    def move(self, ):
        tecla = pygame.key.get_pressed()
        if tecla[JOGADOR_KEYUP[self.name]] and self.rect.top > 0:
            self.rect.centery -= VELOCIDADE[self.name]
        if tecla[JOGADOR_KEYDOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += VELOCIDADE[self.name]
        if tecla[JOGADOR_KEYLEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= VELOCIDADE[self.name]
        if tecla[JOGADOR_KEYRIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += VELOCIDADE[self.name]
        pass

    def tiro(self):
        self.delay_tiro -= 1
        if self.delay_tiro == 0:
          self.delay_tiro = DELAY_TIRO[self.name]
          pressed_key = pygame.key.get_pressed()
          if pressed_key[JOGADOR_TIRO[self.name]]:
             return tirojogador(name= f'{self.name}tiro', position=(self.rect.centerx, self.rect.centery))
