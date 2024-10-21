import json
import pandas as pd
import numpy as np
from typing import Tuple, Optional
from model1 import Model1
from game import Game


with open('backend/teams.json', 'r') as f:
    TEAMS = json.load(f)

def get_teams_stats(games: list[Game]):
    COLS = [
        "PTS", "AST", "DREB", "OREB", "3PM", "3PA", "FGM", "FGA",
        "FTM", "FTA", "BLK", "STL", "TO", "PF", "WIN%"
    ]
    X = pd.DataFrame(data=None, columns=COLS)
    for i, game in enumerate(games):
        h = TEAMS[str(game.home_team_id)]["stats"]
        a = TEAMS[str(game.away_team_id)]["stats"]
        X.loc[i] = np.subtract(h, a)
    print(X)
    return X

def publish_data(games: list[Game], y: Optional[list[Tuple[float, float]]]=None):
    body = {}
    if not y is None:
        for i, game in enumerate(games):
            game.prediction = y[i][0]
            
            body[game.game_id] = {}
            body[game.game_id]["game_id"] = game.game_id
            body[game.game_id]["home_team_id"] = str(game.home_team_id)
            body[game.game_id]["home_team_name"] = game.home_team_name
            body[game.game_id]["away_team_id"] = str(game.away_team_id)
            body[game.game_id]["away_team_name"] = game.away_team_name
            body[game.game_id]["prediction"] = game.prediction
            body[game.game_id]["home_team_logo"] = game.home_team_logo
            body[game.game_id]["away_team_logo"] = game.away_team_logo

            print(game)

    with open("backend/today.json", "w") as f:
        json.dump(body, f, indent=4)
    
if __name__ == "__main__":
    games = Game.get_todays_games()
    if games:
        X = get_teams_stats(games)
        y = Model1().make_preds(X)
        publish_data(games, y)
    else:
        publish_data(games, None)
        print("No games today")