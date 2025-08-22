import pygame

COR_ROXA = (113, 89, 193)
COR_PRETO = (163,73,164)
COR_VERDE = (181,230,29)

INTERFACE = ('NOVO JOGO',
             'C0OPERATIVO',
             'COMPETITIVO',
             'PONTOS',
             'SAIR')

DELAY_TIRO = {
    'jogador1':20,
    'jogador2':15,
    'inimigo1':100,
    'inimigo2':200,
}

VIDA = {
    'fundo0': 999,
    'fundo1': 999,
    'fundo2': 999,
    'fundo3': 999,
    'fundo4': 999,
    'fundo5': 999,
    'fundo6': 999,
    'jogador1':300,
    'jogador1tiro': 1,
    'jogador2':300,
    'jogador2tiro': 1,
    'inimigo1': 50,
    'inimigo1tiro': 1,
    'inimigo2': 60,
    'inimigo2tiro': 1,
}

VELOCIDADE = {
    'fundo0':0,
    'fundo1':1,
    'fundo2':2,
    'fundo3':3,
    'fundo4':4,
    'fundo5':3,
    'fundo6':6,
    'jogador1':3,
    'jogador1tiro':1,
    'jogador2':3,
    'jogador2tiro':1,
    'inimigo1':1,
    'inimigo1tiro': 5,
    'inimigo2':1,
    'inimigo2tiro': 3,
}

JOGADOR_KEYUP = {'jogador1': pygame.K_UP,
                 'jogador2': pygame.K_w}
JOGADOR_KEYDOWN = {'jogador1': pygame.K_DOWN,
                 'jogador2': pygame.K_s}
JOGADOR_KEYLEFT = {'jogador1': pygame.K_LEFT,
                 'jogador2': pygame.K_a}
JOGADOR_KEYRIGHT = {'jogador1': pygame.K_RIGHT,
                 'jogador2': pygame.K_d}
JOGADOR_TIRO = {'jogador1': pygame.K_RCTRL,
                'jogador2': pygame.K_LCTRL}

WIN_WIDTH = 500
WIN_HEIGHT = 350
EVENTO_INIMIGO = pygame.USEREVENT + 1
TEMPO_SPAWN = 4000