from Diagramá.Const import VELOCIDADE, WIN_WIDTH, DELAY_TIRO
from Diagramá.entity import entity
from Diagramá.tiroinimigo import tiroinimigo


class inimigo(entity):
    def __init__(self, name: str, position: tuple):
      super().__init__(name, position)
      self.delay_tiro = DELAY_TIRO[self.name]

    def move(self, ):
        self.rect.centerx -= VELOCIDADE[self.name]


    def tiro(self):
        self.delay_tiro -= 1
        if self.delay_tiro == 0:
          self.delay_tiro = DELAY_TIRO[self.name]
          return tiroinimigo(name=f'{self.name}tiro', position=(self.rect.centerx, self.rect.centery))