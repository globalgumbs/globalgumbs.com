// Game.js
import React from 'react';
import './css/Game.css';

function Game({homeTeam, homeLogo, homePercentage, awayTeam, awayLogo, awayPercentage}) {
  return (
    <div className="game">
      <div className="team-container">
        <img className="team-logo" src={homeLogo} />
        <div className="team-info">
          <div className="team">{homeTeam}</div>
          <p className="percentage">{homePercentage}%</p>
        </div>
      </div>
      
      <p className="vs">@</p>
      
      <div className="team-container">
        <div className="team-info">
          <div className="team">{awayTeam}</div>
          <p className="percentage">{awayPercentage}%</p>
        </div>
        <img className="team-logo" src={awayLogo} />
      </div>
      <div style={{ borderBottom: '1px solid black' }}></div>
    </div>
  );
}

export default Game;
