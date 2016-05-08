class GameObject(object):
    
    def __init__(self, x, y, image, life):        
        self.x = x
        self.y = y
        self.image = image
        self.life = life
        
    
    # Método que move o gameobject
    def move(self, speedX, speedY):
        self.x += speedX
        self.y += speedY
    
    
    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image

    def setLife(self, life):
        self.life = life

    def getLife(self):
        return self.life

    
    
