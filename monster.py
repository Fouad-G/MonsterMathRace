import pygame

class Monster:
    def __init__(self, x, y, speed,monster_image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image_1 = monster_image  # Lädt das GIF



        self.width = self.image_1.get_width()
        self.height = self.image_1.get_height()

    def move(self):
        """Bewegt das Monster nach rechts."""
        self.x += self.speed


    def draw(self, screen):
        """Zeichnet das Monster mit dem GIF an seiner Position."""
        screen.blit(self.image_1, (self.x, self.y))
