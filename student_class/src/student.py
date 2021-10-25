class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        
    def talk(self):
        return "I can talk!"

    def say_favourite_language(self,fav_language):
        student_fav_language = "I love " + fav_language
        return student_fav_language
    


# class Team: 
#     def __init__(self, name, players, coach):
#         self.name = name
#         self.players = players
#         self.coach = coach
#         self.points = 0

#     def add_player(self, name):
#         team["name"].append(name)
    
#     def has_player(self, player):
#         if player == Team["players"]:
#             return True 
#         else:
#             return False

#     def play_game(self, )
    