import json

with open('backend/scripts/wins.txt', 'r') as f:
    lines = f.readlines()
with open('backend/teams.json', 'r') as f:
    teams_dict = json.load(f)

#tuples = []
for line in lines:
    team = line.split("--")[1][:3]
    wins = (line.split("\n")[-2].split(" ")[-1].split("0")[-1])
    for k, v in teams_dict.items():
        if v["abbreviation"] == team:
            team = teams_dict[k]["teamName"]
            teams_dict[k]["stats"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, float(wins)]
            teams_dict[k]["logo"] = ""
            teams_dict[k]["gamesPlayed"] = 0
            break
    
    teams_dict["1610612761"]["stats"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5]
#    tuples.append((int(k), team, float(wins)))
with open('backend/teams.json', 'w') as f:
    json.dump(teams_dict, f, indent = 4, ensure_ascii=False)

print(teams_dict)