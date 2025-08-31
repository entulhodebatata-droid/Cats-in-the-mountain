#!/usr/bin/python
# -*- coding: utf-8 -*-
from Diagramá.Const import WIN_WIDTH, VELOCIDADE
from Diagramá.entity import entity


class fundo(entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= VELOCIDADE[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
