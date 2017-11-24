class Player:
    def __init__(self,user):
        self.user = user
        self.healthscore = 5
        self.key = 0

    def hurtHealth(self):
        self.healthscore = self.healthscore - 1
        return self.healthscore

    def giveKey(self):
        self.key = self.key + 1
        return self.key
