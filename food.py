from turtle import Turtle
import random


# Klasa Food je izvedena iz klase Trutle
class Food(Turtle):

# Ovo je poziv konstruktora nadklase (Turtle) kako bi se prvo inicijalizirala klasa roditelja.
# Klasa "Food" nasljeđuje sve osobine i metode klase "Turtle".
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


# Ova metoda služi za osvježavanje pozicije hrane.
# Svaki put kad se zmija "pojede" hranu, generira novu poziciju hrane.
# Metoda generira nasumične koordinate (x, y) unutar granica (-280, -280) do (280, 280) i postavlja poziciju hrane na te nove koordinate.
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
