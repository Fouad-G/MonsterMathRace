import random
import pygame
import time
from minispiel import Minispiel
class KopfrechenSpiel(Minispiel):
    def __init__(self):
        self.zahl1 = random.randint(1, 10)
        self.zahl2 = random.randint(1, 10)
        self.operator = random.choice(["+", "-", "*"])
        self.loesung = eval(f"{self.zahl1} {self.operator} {self.zahl2}")
        self.optionen = [self.loesung, self.loesung + random.randint(1, 3), self.loesung - random.randint(1, 3)]
        random.shuffle(self.optionen)
        self.round_winner=None

    def start(self, player,player_opp,spieler_name):
        """Zeigt eine Rechenaufgabe an und prüft die Antwort."""
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 50)

        popup_rect = pygame.Rect(0, 0, 400, 300)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect)
        pygame.draw.rect(screen, (0, 0, 0), popup_rect,5)

        spieler_text = font.render(f"{spieler_name} ist dran!", True, ("#98bd8e"))
        screen.blit(spieler_text, (10, 10))
        frage_text = font.render(f"{self.zahl1} {self.operator} {self.zahl2} = ?", True, (0, 0, 0))
        screen.blit(frage_text, (10, 50))

        buttons = []
        for i, option in enumerate(self.optionen):
            button_rect = pygame.Rect(10, 100 + i * 60, 300, 50)
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            text = font.render(str(option), True, (0, 0, 0))
            screen.blit(text, (button_rect.x + 20, button_rect.y + 10))
            buttons.append((button_rect, option))

        pygame.display.update()

        start_time = time.time()
        while time.time() - start_time < 2:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button_rect, option in buttons:
                        if button_rect.collidepoint(event.pos):
                            if option == self.loesung:
                                self.round_winner = player
                                return self.round_winner 
                            elif option != self.loesung:
                                self.round_winner = player_opp
                                return self.round_winner 
                            
        if self.round_winner is None:
            self.round_winner = player_opp
        return self.round_winner  # ❗ Nach Timeout gewinnt der Gegner automatisch   
    
    def start_2(self, player,player_opp,spieler_name):
        """Zeigt eine Rechenaufgabe an und prüft die Antwort."""
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 50)

        popup_rect = pygame.Rect(1080, 0, 400, 300)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect)
        pygame.draw.rect(screen, (0, 0, 0), popup_rect,5)

        spieler_text = font.render(f"{spieler_name} ist dran!", True, ("#98bd8e"))
        screen.blit(spieler_text, (1080+10, 10))
        frage_text = font.render(f"{self.zahl1} {self.operator} {self.zahl2} = ?", True, (0, 0, 0))
        screen.blit(frage_text, (1080+10, 50))

        buttons = []
        for i, option in enumerate(self.optionen):
            button_rect = pygame.Rect(1080+10, 100 + i * 60, 300, 50)
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            text = font.render(str(option), True, (0, 0, 0))
            screen.blit(text, (button_rect.x + 20, button_rect.y + 10))
            buttons.append((button_rect, option))

        pygame.display.update()

        start_time = time.time()
        while time.time() - start_time < 2:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button_rect, option in buttons:
                        if button_rect.collidepoint(event.pos):
                            if option == self.loesung:
                                self.round_winner = player
                                return self.round_winner
                                
                            elif option != self.loesung:
                                self.round_winner = player_opp
                                return self.round_winner 
                            
        if self.round_winner is None:
            self.round_winner = player_opp
        return self.round_winner  # ❗ Nach Timeout gewinnt der Gegner automatisch  

    def check_round_winner(self):
        return self.round_winner 
