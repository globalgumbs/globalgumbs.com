import React, { useEffect, useState } from 'react';
import './App.css';
import Game from './components/Game.js'


function App() {
  const [games, setGames] = useState([]);

  useEffect((games) => {
    fetch('http://localhost:5000/update')
      .then((response) => response.json())
      .then((data) => setGames(data))
      .then(console.log(games))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);


  return (
    <div className="App">
      <div className="gg">GG.</div>
      <h1>Games</h1>
      {games.map((game, index) => (
        <Game
          key={index}
          homeTeam={game.homeTeam}
          homeLogo={game.homeLogo}
          homePercentage={game.homePercentage}
          awayTeam={game.awayTeam}
          awayLogo={game.awayLogo}
          awayPercentage={game.awayPercentage}
        />
      ))}
    </div>
  );
}

export default App;