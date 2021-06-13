class Player:
    def __init__(self, name, atk):
        self.hp = 100
        self.atk = atk
        self.name = name
    
    def attack(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.atk

p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(p2)
print(p2.hp)