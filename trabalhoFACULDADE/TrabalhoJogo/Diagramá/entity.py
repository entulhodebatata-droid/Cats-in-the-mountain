#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image

from Diagramá.Const import VIDA


class entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left = position[0], top = position[1])
        self.speed = 0
        self.health = VIDA[self.name]

    @abstractmethod
    def move(self, ):
        pass
