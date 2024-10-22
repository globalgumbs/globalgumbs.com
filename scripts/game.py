from typing import Optional
import requests
import json

class Game:
    """Game class to store game information"""
    def __init__(self, home_team_id: str, away_team_id: str, game_id: str):
        self.game_id: str = game_id
        self.home_team_id: str = home_team_id  
        self.away_team_id: str = away_team_id 
        
        with open("./artifacts/teams.json", "r") as f:
            TEAMS = json.load(f)
        self.home_team_name: str = TEAMS[str(home_team_id)]["teamName"]
        self.away_team_name: str = TEAMS[str(away_team_id)]["teamName"]
        self.home_team_logo: str = TEAMS[str(home_team_id)]["logo"]
        self.away_team_logo: str = TEAMS[str(away_team_id)]["logo"]

        self.winner: Optional[int] = None         
        self.prediction: Optional[float] = None

    @staticmethod
    def get_todays_games():
        req = requests.get("https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json").json()
        # with open('./archive/todaysScoreboard_00.json', 'r') as f:
        #     req = json.load(f)
        games = []
        for game in req["scoreboard"]["games"]:
            home_team_id = game["homeTeam"]["teamId"]
            away_team_id = game["awayTeam"]["teamId"]
            game_obj = Game(
                game_id = game["gameId"],
                home_team_id = home_team_id,
                away_team_id = away_team_id
            )         
            games.append(game_obj)
       
#       for game in games: print(game)
        return games

    def __str__(self):
        return (
            f"Game ID: {self.game_id} | Home Team: {self.home_team_id} - {self.home_team_name} | Away Team ID: {self.away_team_id} - {self.away_team_name} | " + 
            f"Predicted Winner: {self.prediction} | Actual Winner: {self.winner}"
        )    