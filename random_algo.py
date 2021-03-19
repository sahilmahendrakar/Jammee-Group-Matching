from individual import Individual
import numpy as np
import random

# Limited points to allocate for desires (probs better because it encourages people to differentiate)
# Normalize sum after (maybe not as good since everybody migt just wanna put 10)

#Matrix mean squared error, not quite what we want cause only compares one individual to another, we want to compare all individuals' skills./desires to eacho ther
def score_team_v2(team):
    A = np.row_stack([i.skills for i in team])
    B = np.row_stack([i.desires for i in team])
    return np.square(np.subtract(A, B)).mean()

#Score: 1/n*(S - D)^2 where S is the average of the teams skills and D is the average of the desires of the teams, and n is number of categories
def score_team(team):
    skills_sum = np.copy(team[0].skills)
    for i in range(1, len(team)):
        skills_sum += team[i].skills[:]
    skills_avg = skills_sum / len(team)
    
    desires_sum = np.copy(team[0].desires)
    for i in range(1, len(team)):
        desires_sum += team[i].desires[:]
    desires_avg = desires_sum / len(team)

    score = 0
    for i in range(0, len(skills_avg)):
        score += ((skills_avg[i] - desires_avg[i])**2)/len(skills_avg)
    
    return score

#Average score of all teams
def score_teams(teams):
    score = 0
    for team in teams:
        score += score_team(team)
    return score/len(teams)

def generate_random_teams(individuals, team_size):
    teams = []
    random.shuffle(individuals)
    for i in range(0, len(individuals), team_size):
        teams.append(individuals[i:i+team_size])
    return teams

#inputs: list of individuals, size of team
def random_matching(individuals, team_size, iterations):
    best_teams = generate_random_teams(individuals, team_size)
    best_score = score_teams(best_teams)

    for i in range(iterations):
        cur_teams = generate_random_teams(individuals, team_size)
        #print(cur_teams)
        score = score_teams(cur_teams)
        #print("Score: ", score)
        if score < best_score:
            best_teams = cur_teams
            best_score = score

    return (best_teams, best_score)
    

individuals = []
for i in range(50):
    skills = np.random.randint(0, 10, 4)
    desires = np.random.randint(0, 10, 4)
    individuals.append(Individual(i, skills, desires))



best_teams, best_score = random_matching(individuals[:] , 5, 10000)

for i in individuals:
    print(i)

print("Best teams: " + str([[individual.id for individual in team] for team in best_teams]))
print("Score: " + str(best_score))