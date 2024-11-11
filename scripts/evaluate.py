from game import Game
from typing import Optional
import json
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

LOG_PATH = "./artifacts/log.csv"
TODAY_PATH = "./src/today.json"
with open("./artifacts/teams.json", "r") as f: teams =json.load(f)

def get_results(date: str) -> Optional[dict[str, dict[str, int]]]:
    """ Date: str in form '10/17/2024' ------------- Returns {game_id: winner (0 for home | 1 for away)} for all games played on the input date """
    url = f"https://core-api.nba.com/cp/api/v1.8/feeds/gamecardfeed?gamedate={date}&platform=web"
    headers = {
        "sec-ch-ua-platform": "\"Android\"",
        "Referer": "https://www.nba.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?1",
        "Ocp-Apim-Subscription-Key": "747fa6900c6c4e89a58b81b72f36eb96",
        "Accept": "application/json",
        "DNT": "1",
        "x-postal-code": "21114"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch NBA data: {response.status_code}")
        return None
    body = response.json()
    
    results = {date:{}}
    try:
        for dict in body["modules"][0]["cards"]:
            if dict["cardData"]["homeTeam"]["score"] > dict["cardData"]["awayTeam"]["score"]:
                results[date][dict["cardData"]["gameId"]] = 0
            else:
                results[date][dict["cardData"]["gameId"]] = 1
    except:
        print("No games on ", date)
        return None
#    print(results)
    return results


def eval_preds(results: Optional[dict[str, dict[str, int]]]) -> Optional[pd.DataFrame]:
    if not results:
        print("No results to evaluate")
        return None
    
    with open(TODAY_PATH, "r") as f:
        games = json.load(f)
    date = list(results.keys())[0]
    if not games:
        print("No games on ", date)
        return None
    with open(LOG_PATH, "r") as f:
        log = pd.read_csv(f, dtype={"game_id":str})
    df = pd.DataFrame(data=[], columns=["game_id", "home_team_id", "home_team_name", "away_team_id", "away_team_name", "prediction", "winner", "date"])
    for game_id in list(results[date].keys()):
        try: 
            df.loc[len(df)] = [
                game_id,
                games[game_id]["home_team_id"],
                teams[games[game_id]["home_team_id"]]["teamName"],
                games[game_id]["away_team_id"],
                teams[games[game_id]["away_team_id"]]["teamName"],
                games[game_id]["prediction"],
                results[date][game_id],
                datetime.strptime(date, '%m/%d/%Y').strftime('%m-%d-%Y')
            ]
        except:
            print("Game ID not found in today.json")
            continue
    log = pd.concat([log, df], ignore_index=True)
    log.to_csv(LOG_PATH, index=False)
    print(df)
    return df

def get_boxscore(game_id: str) -> Optional[dict[str, list]]:
    url = f"https://cdn.nba.com/static/json/liveData/boxscore/boxscore_{game_id}.json"
    headers = {
        "authority": "cdn.nba.com",
        "method": "GET",
        "path": f"/static/json/liveData/boxscore/boxscore_{game_id}.json",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "dnt": "1",
        "if-modified-since": "Sat, 16 Jan 2021 05:01:03 GMT",
        "if-none-match": "\"3a472395ed5b420f4c5e88dc2678a7d8\"",
        "priority": "u=0, i",
        "referer": "https://www.nba.com/",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
   
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch NBA data: {response.status_code}")
        return None
    # with open("backend/boxscore.json", "r") as f:
    #     body = json.load(f)
    body = response.json()
#    print(response.status_code)
    
    home_team_id = str(body["game"]["homeTeam"]["teamId"])
    away_team_id = str(body["game"]["awayTeam"]["teamId"])
    stats = {home_team_id:[], away_team_id:[]}
    for team in [("homeTeam", home_team_id), ("awayTeam", away_team_id)]:
        stats[team[1]].append(body["game"][team[0]]["statistics"]["points"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["assists"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["reboundsTeamDefensive"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["reboundsTeamOffensive"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["fieldGoalsMade"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["fieldGoalsAttempted"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["threePointersMade"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["threePointersAttempted"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["freeThrowsMade"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["freeThrowsAttempted"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["blocks"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["steals"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["turnovers"])
        stats[team[1]].append(body["game"][team[0]]["statistics"]["foulsPersonal"])
    return stats
        
def update_stats_table(df: Optional[pd.DataFrame]) -> bool:
    if df is None:
        print("No data to update")
        return False
    updated = []
    for i, row in df.iterrows():
        try:
            game_id = row["game_id"]
            home_team_id = str(row["home_team_id"])
            away_team_id = str(row["away_team_id"])
            boxscore = get_boxscore(game_id)            
            if not boxscore:
                return False
            
            pm = np.subtract(boxscore[home_team_id], boxscore[away_team_id]).tolist()
            
            for count, team_id in enumerate([home_team_id, away_team_id]):
                if team_id not in teams:  # Ensure we only update existing teams
                    print(f"Team ID {team_id} not found.")
                    continue
                
                old_stats = teams[team_id]["stats"]
                n = teams[team_id]["gamesPlayed"]
                new_stats = []
                
                # Reverse point margin for the away team
                if count == 1:
                    pm = [-num for num in pm]
                    
                # Update statistics using weighted average
                for j in range(len(pm)):
                    new_stats.append((old_stats[j] * n + pm[j]) / (n + 1))
                
                new_stats.append(old_stats[-1])
                
                teams[team_id]["stats"] = new_stats
                teams[team_id]["gamesPlayed"] += 1
                updated.append(teams[team_id]["teamName"])
                
        except Exception as e:
            print("Failed to update stats for game:", game_id)
            print(e)
    with open("./artifacts/teams.json", "w") as f:  # Ensure the path and file extension
        json.dump(teams, f, indent=4)
    print("Updated stats for:", updated)
    return True


def create_df(): # Run this once to create the log.csv file
    df = pd.DataFrame(data=[], columns=["game_id", "home_team_id", "home_team_name", "away_team_id", "away_team_name", "prediction", "winner", "date"])
    df.to_csv(LOG_PATH, index=False)

if __name__ == "__main__":
    yesterday = (datetime.now() - timedelta(1)).strftime('%m/%d/%Y')
    results = get_results(yesterday)
    print(results)
    df = eval_preds(results)
    update_stats_table(df)