# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import awsgi

app = Flask(__name__)
CORS(app)

BASE_ROUTE = "/evaluate"
@app.route('/evaluate', methods=['GET'])
def get_games():
    games = [
        {
            "homeTeam": "LAL",
            "homeLogo": "https://path-to-lakers-logo.png",
            "homePercentage": 78,
            "awayTeam": "WAS",
            "awayLogo": "https://path-to-wizards-logo.png",
            "awayPercentage": 22
        },
        {
            "homeTeam": "LAL",
            "homeLogo": "https://path-to-lakers-logo.png",
            "homePercentage": 78,
            "awayTeam": "WAS",
            "awayLogo": "https://path-to-wizards-logo.png",
            "awayPercentage": 22
        }
    ]
    return jsonify(games)

def handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)