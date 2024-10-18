class Game:
    def __init__(self, home_team_id, away_team_id, winner=None, prediction=None):
        self.home_team_id = home_team_id  
        self.away_team_id = away_team_id 
        self.winner = winner               
        self.prediction = prediction

    def __str__(self):
        return (
            f"Home Team ID: {self.home_team_id} | Away Team ID: {self.away_team_id} | " + 
            f"Predicted Winner: {self.prediction} | Actual Winner: {self.winner}"
        )