import json
import data_retrieval
import pandas as pd

# Define columns (which will be same for db)
CATEGORIES = ['date', 'home_team', 'away_team', 'home_pts', 'away_pts', 'home_ast', 'away_ast', 'home_dreb', 'away_dreb', 'home_oreb', 'away_oreb', 'home_made_fg', 'away_made_fg', 'home_att_fg', 'away_att_fg', 'home_made_3fg', 'away_made_3fg', 'home_att_3fg', 'away_att_3fg', 'home_made_ft', 'away_made_ft', 'home_att_ft', 'away_att_ft', 'home_blocks', 'away_blocks', 'home_steals', 'away_steals', 'home_to', 'away_to', 'home_pf', 'away_pf']

def format_data() -> dict:
    # Load data from the json files
    box_scores = read_json_data("scripts/data/box_score_data.json")
    game_data = data_retrieval.dedupe(read_json_data("scripts/data/game_data.json"))
    box_scores_dates = [item[1] for item in enumerate(box_scores)]

    # Collect data and format into dict of lists
    data = {}
    for cat in CATEGORIES:
        data[cat] = []
    i, j = 0, 0
    while i < len(box_scores_dates):
        while j < len(list(enumerate(game_data))):
            day = game_data[j]["start_time"][:10]
            if day not in box_scores_dates:
                j += 1
            elif day == box_scores_dates[i]:
                # grab all of the necessary data in here
                home_team = game_data[j]["home_team"]
                away_team = game_data[j]["away_team"]

                data["date"].append(day)

                data["home_team"].append(home_team)
                data["away_team"].append(away_team)

                data["home_pts"].append(game_data[j]["home_team_score"])
                data["away_pts"].append(game_data[j]["away_team_score"])

                j += 1
            else:
                break
        i += 1

    # with open('data/temp.json', '+r') as file:
    # #        json.dump(data, file)
    #         data = json.load(file)

    for m in range(len(data["date"])):  
        date = data["date"][m]
        home_team = data["home_team"][m]
        away_team = data["away_team"][m]
        
        try:
            # Find home team in box score data
            k = 0
            while home_team != box_scores[date][k]["team"]:
                k += 1

            # Find away team in box score data
            l = 0
            while away_team != box_scores[date][l]["team"]:
                l += 1
        except:
                print(date, ": ", home_team, " vs ", away_team, "matchup was not found")
                continue

    #    print(str(m), date, home_team, " vs ", away_team)

        data["home_ast"].append(box_scores[date][k]["assists"])
        data["home_dreb"].append(box_scores[date][k]["defensive_rebounds"])
        data["home_oreb"].append(box_scores[date][k]["offensive_rebounds"])
        data["home_made_fg"].append(box_scores[date][k]["made_field_goals"])
        data["home_att_fg"].append(box_scores[date][k]["attempted_field_goals"])
        data["home_made_ft"].append(box_scores[date][k]["made_free_throws"])
        data["home_att_ft"].append(box_scores[date][k]["attempted_free_throws"])
        data["home_made_3fg"].append(box_scores[date][k]["made_three_point_field_goals"])
        data["home_att_3fg"].append(box_scores[date][k]["attempted_three_point_field_goals"])
        data["home_blocks"].append(box_scores[date][k]["blocks"])
        data["home_steals"].append(box_scores[date][k]["steals"])
        data["home_to"].append(box_scores[date][k]["turnovers"])
        data["home_pf"].append(box_scores[date][k]["personal_fouls"])
            
        data["away_ast"].append(box_scores[date][l]["assists"])
        data["away_dreb"].append(box_scores[date][l]["defensive_rebounds"])
        data["away_oreb"].append(box_scores[date][l]["offensive_rebounds"])
        data["away_made_fg"].append(box_scores[date][l]["made_field_goals"])
        data["away_att_fg"].append(box_scores[date][l]["attempted_field_goals"])
        data["away_made_ft"].append(box_scores[date][l]["made_free_throws"])
        data["away_att_ft"].append(box_scores[date][l]["attempted_free_throws"])
        data["away_made_3fg"].append(box_scores[date][l]["made_three_point_field_goals"])
        data["away_att_3fg"].append(box_scores[date][l]["attempted_three_point_field_goals"])
        data["away_blocks"].append(box_scores[date][l]["blocks"])
        data["away_steals"].append(box_scores[date][l]["steals"])
        data["away_to"].append(box_scores[date][l]["turnovers"])
        data["away_pf"].append(box_scores[date][l]["personal_fouls"])

    return data

def read_json_data(path: str) -> dict:
    with open(path, '+r') as file:
        return json.load(file)


def create_df(data: dict) -> pd.DataFrame:
    # Create Pandas DataFrame to add data into
    df = pd.DataFrame(data=data, index=None, columns=CATEGORIES)
    return df

def unit_test(df: pd.DataFrame) -> bool:
    date = "2021-02-11"
    home_team = "BOSTON CELTICS"
    away_team = "TORONTO RAPTORS"
    home_pts = 120
    away_blocks = 8
    
    # Find a way to assert that these values are true
    return True

    
df = create_df(read_json_data("scripts/data/saved_data.json"))
unit_test(df)

