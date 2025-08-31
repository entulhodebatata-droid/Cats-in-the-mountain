import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from Diagramá.Const import COR_ROXA, SCORE_POS, INTERFACE, COR_ROSA, COR_VERDE
from Diagramá.DBproxy import DBProxy


class Pontos:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/pontos.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, modo_jogo: str, pontos_jogador: list[int]):
        pygame.mixer_music.load('./assets/pontos.mp3')
        pygame.mixer_music.play(-1)
        DB_proxy = DBProxy("DBscore")
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(50, "Vitória!", COR_ROXA, SCORE_POS['title'])
            score = pontos_jogador[0]
            text = 'Adicione seu nome, jogador 1 (4 letras):'

            if modo_jogo == INTERFACE[0]:  # Modo single player
                score = pontos_jogador[0]
            elif modo_jogo == INTERFACE[1]:  # Modo cooperativo (média dos dois)
                score = int((pontos_jogador[0] + pontos_jogador[1]) / 2)
                text = 'Adicione o nome do time (4 letras):'
            elif modo_jogo == INTERFACE[2]:  # Modo competitivo (pega o maior)
                if pontos_jogador[0] < pontos_jogador[1]:
                    score = pontos_jogador[1]
                    text = 'Adicione o nome, vencedor 2;)(4 letras):'
                else:
                    score = pontos_jogador[0]

            self.score_text(20, text, COR_ROSA, SCORE_POS['Entername'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        DB_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(20, name, COR_ROSA, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./assets/pontos.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(30, 'TOP 10 MELHORES', COR_ROSA, SCORE_POS['title'])
        self.score_text(20, 'NAME         SCORE          DATE', COR_VERDE, SCORE_POS['label'])
        db_proxy = DBProxy('DBscore')
        list_score = db_proxy.retrieve_top()
        db_proxy.close()

        for pontos_jogador in list_score:
            id_, name, score, date = pontos_jogador
            self.score_text(20, f'                  {name}             {score: 05d}      {date}', COR_ROSA,
                            SCORE_POS[list_score.index(pontos_jogador)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    elif event.key == pygame.K_r:
                        db = DBProxy("DBscore")
                        db.clear_all_scores()
                        db.close()
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Elephant', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
