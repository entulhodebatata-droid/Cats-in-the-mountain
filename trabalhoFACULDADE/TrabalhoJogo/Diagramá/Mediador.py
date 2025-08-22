from Diagramá.Const import WIN_WIDTH
from Diagramá.entity import entity
from Diagramá.inimigo import inimigo
from Diagramá.tiroinimigo import tiroinimigo
from Diagramá.tirojogador import tirojogador


class Mediador:

    @staticmethod
    def __verify_collision_window(ent: entity): #Só vai funcionar nesta classe
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
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            entity_test = entity_list[i]
            Mediador.__verify_collision_window(entity_test)

    @staticmethod
    def verify_vida(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

