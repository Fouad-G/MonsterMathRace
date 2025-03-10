#Verantwortung:
#✅ Enthält verschiedene Spiele (z. B. Wettrennen, Puzzle, Kampf).
#✅ Bewertet Monster basierend auf Eigenschaften (z. B. Geschwindigkeit für ein Rennen).

from abc import ABC, abstractmethod

class Minispiel(ABC):
    """Abstrakte Klasse für Minispiele."""
    
    @abstractmethod
    def start(self, player,player_name):
        """Startet das Minispiel für einen bestimmten Spieler."""
        pass

    @abstractmethod
    def check_round_winner(self):
        """Prüft, ob das Minispiel einen Gewinner hat."""
        pass
