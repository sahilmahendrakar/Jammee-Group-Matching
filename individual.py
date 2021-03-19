class Individual:
    def __init__(self, i, skills, desires):
        self.id = i
        self.skills = skills
        self.desires = desires
    #frontend, backend, data science, business
    def __str__(self):
        return "Id: " + str(self.id) + ", skills: " + str(self.skills) + ", desires: " + str(self.desires)

    def __repr__(self):
        return "Id: " + str(self.id) + ", skills: " + str(self.skills) + ", desires: " + str(self.desires)
    
