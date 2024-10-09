
class Team:
    name:str
    score:int

    def __init__(self, i_name, i_score):
        self.name = i_name
        self.score = i_score

choice = ""
teams  = []

while(choice != "stop"):
    choice = input("Would you like to stop: ").lower()
    if(choice == "stop"):
        break
    
    name:str = input("Enter the teams name: ")
    score:int = int(input(f"Enter {name}'s score"))

    teams.append(Team(name, score))

winner:Team = Team("", -1)
for i in teams:
    if(i.score > winner.score):
        winner.score = i.score
        winner.name = i.name

print(f"The winner is {winner.name} with a score of {winner.score}")
