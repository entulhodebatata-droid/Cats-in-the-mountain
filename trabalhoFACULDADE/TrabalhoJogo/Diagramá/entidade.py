import random

from Diagramá.Const import WIN_WIDTH, WIN_HEIGHT
from Diagramá.fundo import fundo
from Diagramá.jogador import jogador
from Diagramá.inimigo import inimigo


class entidade:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'fundo1BG':
                list_bg = []
                for i in range(7):
                    list_bg.append(fundo(f'fundo1BG{i}', (0, 0)))
                    list_bg.append(fundo(f'fundo1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'fundo2BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(fundo(f'fundo2BG{i}', (0, 0)))
                    list_bg.append(fundo(f'fundo2BG{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'jogador1':
                return jogador('jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'jogador2':
                return jogador('jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'inimigo1':
                return inimigo('inimigo1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'inimigo2':
                return inimigo('inimigo2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
