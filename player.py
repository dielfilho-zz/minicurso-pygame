from game_object import GameObject

class Player(GameObject):

    def __init__(self, x, y, image, life):
    	# Chamando o contrutor da classe mãe GameObject
        super(Player, self).__init__(x, y, image, life)
        
    # Método que remove a vida do player
    def lossLife(self, count):
        self.life -= count

        