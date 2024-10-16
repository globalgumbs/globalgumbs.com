# app.py
from flask import Flask, jsonify
import boto3
import os

client = boto3.client("dynamodb", region_name="us-east-1")
TABLE = os.environ.get("storageHoopDB")
app = Flask(__name__)


BASE_ROUTE = "/"
@app.get(BASE_ROUTE)
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
    return app(event, context)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)