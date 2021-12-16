import turtle
class Main():#https://touey456.wordpress.com/2017/02/28/python-turtle-module-how-to-get-mouse-coordinates-without-clicking/
    def __init__(self):
        wn = turtle.Screen()
        wn.setup(600, 600)
        screen = wn.getcanvas()
        self.t = turtle.Turtle()
        self.x = 300
        self.y = 300
        self.speed = -1
        screen.bind('<Motion>', self.set_coords)
        self.run()
    def set_coords(self, event):
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            self.t.setposition(self.x-300, (self.y*-1)+300)
m = Main()