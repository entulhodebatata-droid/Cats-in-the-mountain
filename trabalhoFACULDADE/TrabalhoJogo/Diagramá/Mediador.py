from Diagramá.Const import WIN_WIDTH
from Diagramá.entity import entity
from Diagramá.inimigo import inimigo
from Diagramá.jogador import jogador
from Diagramá.tiroinimigo import tiroinimigo
from Diagramá.tirojogador import tirojogador


class Mediador:

    @staticmethod
    def __verify_collision_window(ent: entity):  #Só vai funcionar nesta classe
        if isinstance(ent, inimigo):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, tirojogador):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, tiroinimigo):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        colisao = False
        if isinstance(ent1, inimigo) and isinstance(ent2, tirojogador):
            colisao = True
        elif isinstance(ent1, tirojogador) and isinstance(ent2, inimigo):
            colisao = True
        elif isinstance(ent1, jogador) and isinstance(ent2, tiroinimigo):
            colisao = True
        elif isinstance(ent1, tiroinimigo) and isinstance(ent2, jogador):
            colisao = True

        if colisao:  #O true não é necessário, sem ele daria no mesmo.
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __dar_pontos(Inimigo: inimigo, entity_list: list[entity]):
        if Inimigo.last_dmg == 'jogador1tiro':
            for ent in entity_list:
                if ent.name == 'jogador1':
                    ent.score += Inimigo.score
        elif Inimigo.last_dmg == 'jogador2tiro':
            for ent in entity_list:
                if ent.name == 'jogador2':
                    ent.score += Inimigo.score

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            entidade1 = entity_list[i]
            Mediador.__verify_collision_window(entidade1)
            for j in range(i + 1, len(entity_list)):  #evita repetições desnecessárias
                entidade2 = entity_list[j]
                Mediador.__verify_collision_entity(entidade1, entidade2)

    @staticmethod
    def verify_vida(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, inimigo):
                    Mediador.__dar_pontos(ent, entity_list)
                entity_list.remove(ent)
