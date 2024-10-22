import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './components/css/App.css';
import Home from './components/Home'
import Nav from './components/Nav'
import Predictions from './components/Predictions'
import Projects from './components/Projects'


function App() {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/projects" element={<Projects />} /> 
        <Route path="/predictions" element={<Predictions />} />
      </Routes>
    </Router>
  );
}

export default App;