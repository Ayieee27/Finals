class Score:
    def __init__(self,username, score, stages):
        self.username = username
        self.score = score
        self.stages = stages
        pass

    def getscore(self):
        return self.score
    
    def getusername(self):
        return self.username
    
    def getstages(self):
        return self.stages