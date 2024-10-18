import requests
import json
from types import MappingProxyType
from game import Game

with open('teams.json', 'r') as f:
    TEAMS = json.load(f)

 # get("https://api-nba-v1.p.rapidapi.com/games/teamId/1");
def get_todays_games():
    #req = requests.get("https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json").json()
    with open('todaysScoreboard_00.json', 'r') as f:
        req = json.load(f)
    games = []
    for game in req["scoreboard"]["games"]:
        games.append(
            Game(
                home_team_id = game["homeTeam"]["teamId"], 
                away_team_id = game["awayTeam"]["teamId"],
            )
        )
    for game in games: print(game)
    return games

get_todays_games()