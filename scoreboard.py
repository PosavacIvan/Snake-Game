from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

#Ovo je konstruktor klase. Pri stvaranju objekta klase, ovaj konstruktor će se izvršiti.
# U njemu se inicijaliziraju atributi i pozivaju metode kako bi se postavio početni položaj i stanje scoreboard-a.
# Također, učitava se "data.txt" datoteka koja sadrži high score rezultat.
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
#metoda koja aužurira trenutno stanje score-a i high score-a.
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

#Ova metoda se poziva kada igra završi i provjerava je li postignut novi najbolji rezultat,
#ako je onda se u datoteku data.txt zapisuje taj novi najveći rezultat.
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_scoreboard()

#Izvršava se kada igra završi i na ekranu prikazuje "Game Over"
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

#Ova metoda se poziva svaki put kada igrač postigne bod.
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        self.reset()


