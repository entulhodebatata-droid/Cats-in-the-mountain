#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Diagramá.Const import WIN_WIDTH, WIN_HEIGHT
from Diagramá.fundo import fundo
from Diagramá.jogador import jogador
from Diagramá.inimigo import inimigo


class entidade:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'fundo':
              list_bg = []
              for i in range(7):
                 list_bg.append(fundo(f'fundo{i}',(0,0)))
                 list_bg.append(fundo(f'fundo{i}',(WIN_WIDTH,0)))
              return list_bg

            case 'jogador1':
                return jogador('jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'jogador2':
                return jogador('jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'inimigo1':
                return inimigo('inimigo1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'inimigo2':
                return inimigo('inimigo2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

