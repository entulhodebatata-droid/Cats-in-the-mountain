#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from Diagramá.entidade import entidade
from Diagramá.entity import entity


class niveis:
    def __init__(self, window, name, modo_jogo):
        self.window = window
        self.name = name
        self.modo_jogo = modo_jogo
        self.entity_list: list[entity] = []
        self.entity_list.extend(entidade.get_entity('fundo'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
