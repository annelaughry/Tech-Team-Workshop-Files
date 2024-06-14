import random

# List of team names
team_names = [
    "Capybara", 
    "Stealth", 
    "Noroc", 
    "Bunsen Burners", 
    "Supernovas", 
    "Lab Rats", 
    "Rocket Riders", 
    "Parkour Science"
]

# Generate random starting scores between 0 and 20 for each team
starting_scores = []
for _ in team_names:
    starting_scores.append(random.randint(0, 20))

# Print initial team scores list
print("Initial team scores list:")
print(starting_scores)

# Combine team_names and starting_scores to create a dictionary
team_scores = dict(zip(team_names, starting_scores))

# Print initial team scores dictionary
print("Initial team scores dictionary:")
print(team_scores)

# Increase the Supernovas score by 50 points
team_scores["Supernovas"] += 50

# Change the team name from "Bunsen Burners" to "Burners"
team_scores["Burners"] = team_scores.pop("Bunsen Burners")

# Delete the Burners team from the dictionary
del team_scores["Burners"]

# Function to randomly add or remove scores
def randomly_update_scores(scores):
    for team in scores:
        change = random.randint(-10, 10)  # Random change between -10 and 10
        scores[team] += change

# Randomly update team scores
randomly_update_scores(team_scores)

# Sort teams by score in descending order
sorted_teams = sorted(team_scores.items(), key=lambda x: x[1], reverse=True)

# Print the teams in order from highest to lowest score
print("Teams ordered by score (highest to lowest):")
for team, score in sorted_teams:
    print(f"{team}: {score}")

# Adding player names to each team
team_players = {
    "Capybara": ["Alice", "Bob", "Charlie"],
    "Stealth": ["Dave", "Eve", "Frank"],
    "Noroc": ["Grace", "Heidi", "Ivan"],
    "Supernovas": ["Jack", "Kathy", "Liam"],
    "Lab Rats": ["Mia", "Nina", "Oscar"],
    "Rocket Riders": ["Paul", "Quincy", "Rachel"],
    "Parkour Science": ["Steve", "Trudy", "Uma"]
}

# Print the teams with their players
print("\nTeams and their players:")
for team, players in team_players.items():
    print(f"{team}: {', '.join(players)}")

print(team_scores)