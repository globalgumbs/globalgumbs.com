import React, { useEffect, useState } from 'react';
import './css/App.css';
import './css/Predictions.css';
import Game from './Game';
import data from '../today.json';
import calCurve from './assets/cal_curve.png';

function getDate(date) {
  // MM/DD/YY to weekday, month DD
  const [month, day, year] = date.split("/").map(Number);
  const dateString = new Date(year + 2000, month - 1, day);

  return new Intl.DateTimeFormat("en-US", {
    weekday: "long",
    month: "short",
    day: "numeric",
  }).format(dateString);
}

function Predictions() {
  const date = Object.keys(data).at(0);
  const dateString = getDate(date);
  const [games, setGames] = useState([]);

  useEffect(() => {
    const arr = Object.values(data[date]);
    console.log(arr);
    setGames(arr);
  }, [date]);

  if (Object.keys(data[date]).length === 0) {
    return (
      <div>
        <h1 className='headline'>{dateString}</h1>
        <div className='no-games'>No games today</div>
      </div>
    );
  }

  return (
    <div className="Predictions">
      <h1 className='headline'>{dateString}</h1>
      {games.map((game, index) => (
        <Game
          key={index}
          homeTeam={game.home_team_name}
          homeLogo={game.home_team_logo}
          homePercentage={Math.round((1 - game.prediction) * 100, 2)}
          awayTeam={game.away_team_name}
          awayLogo={game.away_team_logo}
          awayPercentage={Math.round(game.prediction * 100, 2)}
        />
      ))}
      <div className='info-box'>
        <p>
         The featured model is an <b>Artificial Neural Network (ANN)</b> with a Multi-Layer Perceptron (MLP)
         architecture. The features include current season team box
         score statistics and last season's win percentage for each team. Future improvements to the model may 
         involve incorporating player statistics, injury information, and other relevant factors. This approach was inspired by <a 
          href="https://www.sciencedirect.com/science/article/pii/S266682702400015X#appSB"
          target="_blank"
          rel="noreferrer">research
        </a> from Conor Walsh and Alok Joshi of the University of Bath on model selection
         for machine learning in sports analysis.
         The model's Expected Calibration Error (ECE)
         is 4.1%, and it achieves an accuracy of over 65% when tested on NBA games from the 2017-18 
         season through the 2023-24 season. The calibration curve for the model is shown below.
        </p>
        <img src={calCurve} className="cal-curve" alt="Calibration curve for Multi-Layer Perceptron"></img>
      </div>
    </div>
  );
}

export default Predictions;