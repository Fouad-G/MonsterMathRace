import pygame
class MinispielRennen:
    def __init__(self, monster1, monster2, ziel_x):
        self.monster1 = monster1
        self.monster2 = monster2
        self.ziel_x = ziel_x  # X-Position der Ziellinie
        self.winner = None



    def update(self):
        """Bewegt die Monster und prüft, ob eines das Ziel erreicht hat."""

        if self.winner is None:

            if self.monster1.x >= self.ziel_x:
                self.winner = self.monster1

            if self.monster2.x >= self.ziel_x:
                self.winner = self.monster2

    def draw(self, screen):
        """Zeichnet die Monster auf den Bildschirm."""
        self.monster1.draw(screen)
        self.monster2.draw(screen)
   