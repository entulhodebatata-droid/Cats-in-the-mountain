from Diagramá.Const import VELOCIDADE
from Diagramá.entity import entity


class tirojogador (entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centerx += VELOCIDADE[self.name]