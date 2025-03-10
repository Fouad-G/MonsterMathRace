import pygame
from pygame import mixer

from minispielrennen import MinispielRennen
from player import Player
from monster import Monster
from kopfrechenspiel import KopfrechenSpiel
class SpielLogik:
    def __init__(self):
        pygame.init()
        info=pygame.display.Info()
        self.screen_width=info.current_w
        self.screen_high=info.current_h
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_high))
        self.clock = pygame.time.Clock()
        self.running = True
        mixer.init()
        mixer.music.load("/Users/fouadghazal/game_challenge/halalmusik.mp3")
        mixer.music.set_volume(0.5)  # Lautstärke (0.0 - 1.0)
        

        monster1=pygame.image.load("/Users/fouadghazal/game_challenge/frame-1.png")
        monster2=pygame.image.load("/Users/fouadghazal/game_challenge/frame-1 2.png")
        monster1 = pygame.transform.scale(monster1, (300, 300))
        monster2 = pygame.transform.scale(monster2, (300, 300))
        # Hintergrundbild laden
        self.background = pygame.image.load("/Users/fouadghazal/game_challenge/background.png")
# Hintergrundbild skalieren, falls nötig
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_high))
 # Spielernamen abfragen
        player1_name, player2_name = self.get_player_names()
        if player1_name is None or player2_name is None:
            return  # Falls das Fenster geschlossen wurde

        mixer.music.play(-1)  # -1 bedeutet Dauerschleife
        pygame.mixer.music.play(-1, start=1)  # Startet die Musik nach 30 Sekunden
        self.player1 = Player(player1_name, Monster(400, 340-75, 10, monster1))
        self.player2 = Player(player2_name, Monster(400, 450-75, 10, monster2))

        self.rennen = MinispielRennen(self.player1.monster, self.player2.monster, ziel_x=1100)

    def start_game(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(30)

            if self.rennen.winner is  None:  # 🔴 Falls Ziel erreicht, Spiel beenden

                minigame = KopfrechenSpiel()

                # Spieler 1 ist dran
                winner = minigame.start(self.player1, self.player2, self.player1.name)
                if winner == self.player1:
                    for _ in range(10):
                        self.player1.monster.move()
                        self.update()  
                        self.draw()
                        pygame.display.update()
                        pygame.time.delay(50)
                else:
                    for _ in range(10):
                        self.player2.monster.move()
                        self.update()  
                        self.draw()
                        pygame.display.update()
                        pygame.time.delay(50)
                if self.rennen.winner is not  None:  # 🔴 Falls Ziel erreicht, Spiel beenden
                    if self.rennen.winner == self.player1.monster:
                        winner_name = self.player1.name
                    else:
                        winner_name = self.player2.name
                    font = pygame.font.Font(None, 50)
                    text = font.render(f"{winner_name} hat gewonnen!", True, (0, 0, 255))
                    self.screen.blit(text, (self.screen_width // 2 - 100, (self.screen_high // 2 - 50)-200))
                    pygame.display.update()
                minigame = KopfrechenSpiel()
                winner = minigame.start_2(self.player2, self.player1, self.player2.name)
                if winner == self.player2:
                    for _ in range(10):
                        self.player2.monster.move()
                        self.update()  
                        self.draw()
                        pygame.display.update()
                        pygame.time.delay(50)
                else:
                    for _ in range(10):
                        self.player1.monster.move()
                        self.update()  
                        self.draw()
                        pygame.display.update()
                        pygame.time.delay(50)  
                if self.rennen.winner is not None:  # 🔴 Falls Ziel erreicht, Spiel beenden
                    if self.rennen.winner == self.player1.monster:
                        winner_name = self.player1.name
                    else:
                        winner_name = self.player2.name
           

                    font = pygame.font.Font(None, 50)
                    text = font.render(f"{winner_name} hat gewonnen!", True, (0, 0, 255))
                    self.screen.blit(text, (self.screen_width // 2 - 100, (self.screen_high // 2 - 50)-200))
                    pygame.display.update()
            # Spieler 2 ist dran
          

       


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.rennen.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # Hintergrundbild anzeigen
        self.rennen.draw(self.screen)  # Zeichne die Renn-Elemente darüber

            # Spieler-Namen über den Monstern anzeigen
        font = pygame.font.Font(None, 40)
        name1_text = font.render(self.player1.name, True, "#f06228")
        name2_text = font.render(self.player2.name, True, "#3399ff")

        self.screen.blit(name1_text, (self.player1.monster.x + 130, self.player1.monster.y + 145))
        self.screen.blit(name2_text, (self.player2.monster.x + 130, self.player2.monster.y +145))

        pygame.display.update()

    def get_player_names(self):
            """Fragt die Spielernamen ab, bevor das Spiel startet."""
            font = pygame.font.Font(None, 50)
            input_box1 = pygame.Rect(self.screen_width // 2 - 150, self.screen_high // 2 - 60, 300, 50)
            input_box2 = pygame.Rect(self.screen_width // 2 - 150, self.screen_high // 2 + 20, 300, 50)

            player1_name = ""
            player2_name = ""
            active_box = 1

            running = True
            while running:
                self.screen.fill((0, 0, 0))
                text1 = font.render("Spieler 1 Name:", True, (255, 255, 255))
                text2 = font.render("Spieler 2 Name:", True, (255, 255, 255))
                self.screen.blit(text1, (self.screen_width // 2 - 150, self.screen_high // 2 - 100))
                self.screen.blit(text2, (self.screen_width // 2 - 150, self.screen_high // 2 - 20))

                pygame.draw.rect(self.screen, (255, 255, 255), input_box1, 2)
                pygame.draw.rect(self.screen, (255, 255, 255), input_box2, 2)

                name1_text = font.render(player1_name, True, (255, 255, 255))
                name2_text = font.render(player2_name, True, (255, 255, 255))
                self.screen.blit(name1_text, (input_box1.x + 10, input_box1.y + 10))
                self.screen.blit(name2_text, (input_box2.x + 10, input_box2.y + 10))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None, None
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if active_box == 1:
                                active_box = 2
                            else:
                                running = False
                        elif event.key == pygame.K_BACKSPACE:
                            if active_box == 1:
                                player1_name = player1_name[:-1]
                            else:
                                player2_name = player2_name[:-1]
                        else:
                            if active_box == 1:
                                player1_name += event.unicode
                            else:
                                player2_name += event.unicode

            return player1_name, player2_name


if __name__ == "__main__":
    game = SpielLogik()
    game.start_game()