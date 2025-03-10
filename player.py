#Verantwortung:
#✅ Speichert Spielername und aktuelles Monster.
#✅ Kann später erweitert werden (z. B. mehrere Monster besitzen).

class Player:
    def __init__(self, name, monster):
        self.name = name
        self.monster = monster  # Spieler hat ein Monster
