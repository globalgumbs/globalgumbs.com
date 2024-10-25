import React, { useEffect, useState } from 'react';
import './css/App.css';
import './css/Predictions.css';
import Game from './Game';
import data from '../today.json';

function getDate() {
  const today = new Date();
  return today.toDateString();
}

function Predictions() {

  const date = useState([getDate()]);
  const [games, setGames] = useState([]);

  useEffect(() => {
    const arr = Object.values(data);
    console.log(arr);
    setGames(arr);
  }, []);

  if (Object.keys(data).length === 0) {
    return (
      <div>
        <h1 className='pred-header'>No games today</h1>
      </div>
    );
  }

  return (
    <div className="Predictions">
      <h1 className='pred-header'>{date}</h1>
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
    </div>
  );
}

export default Predictions;