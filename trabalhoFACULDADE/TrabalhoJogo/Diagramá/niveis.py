#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame.display
import srt
from pygame import Surface, Rect
from pygame.font import Font
from Diagramá.Const import COR_ROXA, WIN_HEIGHT, INTERFACE, EVENTO_INIMIGO, TEMPO_SPAWN
from Diagramá.Mediador import Mediador
from Diagramá.entidade import entidade
from Diagramá.entity import entity
from Diagramá.inimigo import inimigo
from Diagramá.jogador import jogador


class niveis:
    def __init__(self, window, name, modo_jogo):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.modo_jogo = modo_jogo
        self.entity_list: list[entity] = []
        self.entity_list.extend(entidade.get_entity('fundo'))
        self.entity_list.append(entidade.get_entity('jogador1'))
        if modo_jogo in [INTERFACE[1], INTERFACE[2]]:
            self.entity_list.append(entidade.get_entity('jogador2'))
        pygame.time.set_timer(EVENTO_INIMIGO, TEMPO_SPAWN)


    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (jogador, inimigo)):
                    tiro = ent.tiro()
                    if tiro is not None:
                     self.entity_list.append(tiro)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTO_INIMIGO:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(entidade.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COR_ROXA, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COR_ROXA, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COR_ROXA, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            Mediador.verify_collision(entity_list=self.entity_list)
            Mediador.verify_vida(entity_list=self.entity_list)

        pass

    def level_text(self, text_size: int, text: srt, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Elephant', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
