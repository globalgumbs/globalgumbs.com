import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Home from './Home';
import './css/Nav.css';

const Nav = () => {
    return (
        <div className="nav-container">
            <nav>
                <div className="gg">GG.</div>
                <ul className="nav-list">
                    <li className="nav-list-item">
                        <Link to="/">Home</Link>
                    </li>
                    <li className="nav-list-item">
                        <Link to="/projects">Projects</Link>
                    </li >
                    <li className="nav-list-item">
                        <Link to="/predictions">Predictions</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default Nav;