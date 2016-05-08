from game_object import GameObject

class Enemy(GameObject):

    def __init__(self, x, y, image, life):
    	# Chamando o contrutor da classe mãe GameObject
        super(Enemy, self).__init__(x, y, image, life)

