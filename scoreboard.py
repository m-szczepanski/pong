from turtle import Turtle

TEXT_ALIGN = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.text = "L vs R"
        self.goto(-100, 230)
        self.write(self.l_score, align=TEXT_ALIGN, font=FONT)
        self.goto(100, 230)
        self.write(self.r_score, align=TEXT_ALIGN, font=FONT)
        self.goto(0, 250)
        self.write(self.text, align=TEXT_ALIGN, font=("Courier", 30, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align=TEXT_ALIGN, font=FONT)
        self.goto(100, 230)
        self.write(self.r_score, align=TEXT_ALIGN, font=FONT)
        self.goto(0, 250)
        self.write(self.text, align=TEXT_ALIGN, font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
