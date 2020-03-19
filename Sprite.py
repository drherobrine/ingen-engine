class Sprite:
    x = 0
    y = 0
    animations = []
    animation = ''
    animationframe = 0
    animationstatus = False
    canvas = ''
    name = ''
    def __init__(self, x, y, animations, canvas, name):
        self.x = x
        self.y = y
        self.animations = animations
        self.canvas = canvas
        self.name = name
