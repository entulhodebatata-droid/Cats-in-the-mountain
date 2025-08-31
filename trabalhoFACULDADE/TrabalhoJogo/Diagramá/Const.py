import pygame

WIN_WIDTH = 500
WIN_HEIGHT = 350
EVENTO_INIMIGO = pygame.USEREVENT + 1
TEMPO_SPAWN = 4000
EVENTO_TIMEOUT = pygame.USEREVENT + 2
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

#---------------------------------------
COR_ROXA = (113, 89, 193)
COR_PRETO = (163, 73, 164)
COR_VERDE = (181, 230, 29)
COR_ROSA = (255, 26, 100)
COR_RCLARO = (255, 128, 169)
#---------------------------------------

INTERFACE = ('NOVO JOGO',
             'COOPERATIVO',
             'COMPETITIVO',
             'PONTOS',
             'SAIR')

DELAY_TIRO = {
    'jogador1': 20,
    'jogador2': 15,
    'inimigo1': 100,
    'inimigo2': 200,
}

VIDA = {
    'fundo1BG0': 999,
    'fundo1BG1': 999,
    'fundo1BG2': 999,
    'fundo1BG3': 999,
    'fundo1BG4': 999,
    'fundo1BG5': 999,
    'fundo1BG6': 999,
    'fundo2BG0': 999,
    'fundo2BG1': 999,
    'fundo2BG2': 999,
    'fundo2BG3': 999,
    'fundo2BG4': 999,
    'fundo2BG5': 999,
    'jogador1': 200,
    'jogador1tiro': 1,
    'jogador2': 200,
    'jogador2tiro': 1,
    'inimigo1': 50,
    'inimigo1tiro': 1,
    'inimigo2': 60,
    'inimigo2tiro': 1,
}

SCORE = {
    'fundo1BG0': 0,
    'fundo1BG1': 0,
    'fundo1BG2': 0,
    'fundo1BG3': 0,
    'fundo1BG4': 0,
    'fundo1BG5': 0,
    'fundo1BG6': 0,
    'fundo2BG0': 0,
    'fundo2BG1': 0,
    'fundo2BG2': 0,
    'fundo2BG3': 0,
    'fundo2BG4': 0,
    'fundo2BG5': 0,
    'jogador1': 0,
    'jogador1tiro': 0,
    'jogador2': 0,
    'jogador2tiro': 0,
    'inimigo1': 50,
    'inimigo1tiro': 0,
    'inimigo2': 80,
    'inimigo2tiro': 0,
}

DANO = {
    'fundo1BG0': 0,
    'fundo1BG1': 0,
    'fundo1BG2': 0,
    'fundo1BG3': 0,
    'fundo1BG4': 0,
    'fundo1BG5': 0,
    'fundo1BG6': 0,
    'fundo2BG0': 0,
    'fundo2BG1': 0,
    'fundo2BG2': 0,
    'fundo2BG3': 0,
    'fundo2BG4': 0,
    'fundo2BG5': 0,
    'jogador1': 1,
    'jogador1tiro': 25,
    'jogador2': 1,
    'jogador2tiro': 20,
    'inimigo1': 1,
    'inimigo1tiro': 20,
    'inimigo2': 1,
    'inimigo2tiro': 15,

}

VELOCIDADE = {
    'fundo1BG0': 0,
    'fundo1BG1': 1,
    'fundo1BG2': 2,
    'fundo1BG3': 3,
    'fundo1BG4': 4,
    'fundo1BG5': 3,
    'fundo1BG6': 6,
    'fundo2BG0': 0,
    'fundo2BG1': 1,
    'fundo2BG2': 2,
    'fundo2BG3': 3,
    'fundo2BG4': 4,
    'fundo2BG5': 5,
    'jogador1': 3,
    'jogador1tiro': 1,
    'jogador2': 3,
    'jogador2tiro': 1,
    'inimigo1': 1,
    'inimigo1tiro': 5,
    'inimigo2': 1,
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

SCORE_POS = {
    'title': (WIN_WIDTH / 2, 50),
    'Entername': (WIN_WIDTH / 2, 80),
    'label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),


}
