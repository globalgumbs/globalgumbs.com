import json as json
import time
import random
from datetime import datetime, timezone
import pytz
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_web_scraper.data import OutputWriteOption



SEASONS = []


# function takes list of box score data from basketball_reference_web_scraper and the first day of the regular season and returns a list of strings of all game days in that year's regular season
def get_gamedays(data: list, end: str):
    gamedays = [None]
    for game in enumerate(data):
        day = game[1]["start_time"][0:10]
        if day == end:
            gamedays.append(day)
            break
        elif day not in gamedays:
            gamedays.append(day)
    return gamedays[1:]


# Function takes list of dicts with target seasons file names and end dates, and creates json file with box scores from each game
def create_box_score_json(seasons: dict):
    # Iterate through seasons from 2018-2024
    for season in seasons:
        with open(season["filename"]) as json_file:
            data = json.load(json_file)
        game_days = get_gamedays(data = data, end = season["end_date"])

        # Iterate through each day in the regular season
        for gameday in game_days:
            try:
                year = gameday[0:4]
                month = gameday[5:7]
                day = gameday[8:10]
                with open('box_score_data.json', 'a') as f:
                    f.write("\n\"" + gameday + "\":")
                    f.close()
                client.team_box_scores(day, month, year, OutputType.JSON, output_file_path='box_score_data.json', output_write_option=OutputWriteOption.APPEND)
                with open('box_score_data.json', 'a') as f:
                    f.write(",\n")
                    f.close()
                
                print(month, day, year)
                time.sleep(random.randint(25, 35))
            except:
                print("Loop failed at ", gameday)
                time.sleep(3600)
                

def dedupe(data: dict) -> dict:
    deduped = []
    for item in data:
        if item not in deduped:
            deduped.append(item)
    return deduped


def standardize_dates(path: str) -> dict:
    with open(path) as file:
        data = dedupe(json.load(file))
    est_tz = pytz.timezone("America/New_York")
    for game in data:
        game["start_time"] = str(datetime.fromisoformat(game["start_time"]).replace(tzinfo=timezone.utc).astimezone(est_tz))
    return data
        
def printToFile(data: dict, path: str) -> None:
    with open(path, '+w') as file:
        json.dump(data, file)





# printToFile(data = standardize_dates('data/game_data.json'), path = 'data/game_data.json')
