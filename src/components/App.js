import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './css/App.css';
import Home from './Home'
import Nav from './Nav'
import Predictions from './Predictions'


function App() {
  return (
    <Router>
      <Nav />
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/predictions" element={<Predictions />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;