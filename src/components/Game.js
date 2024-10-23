// Game.js
import React from 'react';
import './css/Game.css';

function Game({homeTeam, homeLogo, homePercentage, awayTeam, awayLogo, awayPercentage}) {
  return (
    <div className="Game">
      <div className="game-container">
        <div className="team-container">
          <img className="team-logo" src={awayLogo} style={{float: 'left'}}/>
          <div className="team-info">
            <div className="team">{awayTeam}</div>
            <p className="percentage">{awayPercentage}%</p>
          </div>
        </div>
        
        <p className="vs">vs</p>
        
        <div className="team-container">
          <div className="team-info">
            <div className="team">{homeTeam}</div>
            <p className="percentage">{homePercentage}%</p>
          </div>
          <img className="team-logo" src={homeLogo} style={{float: 'right'}}/>
        </div>
        <div style={{ borderBottom: '1px solid black' }}></div>
      </div>
    </div>
  );
}

export default Game;
