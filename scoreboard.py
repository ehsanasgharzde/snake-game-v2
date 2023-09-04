from turtle import Turtle


alignment = 'center'
font = ('Courier', 20, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.score = 0
        with open('gamedata.txt') as scoredata:
            self.highscore = int(scoredata.read())
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color('white')
        self.goto(0, 250)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    Highest Score: {self.highscore}", False, alignment, font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('gamedata.txt', 'w') as scoredata:
                scoredata.write(str(self.score))
        self.score = 0
        self.updatescoreboard()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", False, alignment, font)

    def scoretrack(self):
        self.score += 1
        self.updatescoreboard()
        