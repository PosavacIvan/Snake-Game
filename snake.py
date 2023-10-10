from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

#Konstruktor klase
#Pri stvaranju objekta klase, inicijalizira se prazna lista segmenata,
# zatim se poziva metoda za kreiranje zmije koja kreira segmente
# i na kraju se glava zmije postavlja kao prvi segment u listi segmenata zmije
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

#Ova metoda služi za produljenje zmije, dodavanje novog segmenta na kraj(rep)
#Taj novi segment će biti postavljen na poziciju posljednjeg segmenta u listi
    def extend(self):
        self.add_segment(self.segments[-1].position())

#Ova metoda pomiće zmiju prema naprijed za udaljenost definiranu konstantom
#Kreće se od repa zmije prema glavi tako što svaki segment preuzima poziciju svog prethodnika,
#a glava se pomiće prema naprijed.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

#Ovdje su definirane metode zabrane kretanja zmije
#Ako zmija ide gore ne može se okrenuti prema dola već samo lijevo i desno kako nebi pojela sama sebe.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
