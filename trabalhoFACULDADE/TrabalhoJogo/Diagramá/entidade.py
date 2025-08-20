#!/usr/bin/python
# -*- coding: utf-8 -*-
from Diagramá.Const import WIN_WIDTH
from Diagramá.fundo import fundo


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

