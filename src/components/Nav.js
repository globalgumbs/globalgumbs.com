import { React } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './css/Nav.css';

function Nav() {
    const location = useLocation();

    const linkStyle = (path) => ({
        textDecoration: location.pathname === path ? 'underline' : 'none',
        color: location.pathname === path ? 'rgb(148, 194, 206)' : 'black',
    });

    return (
        <div className="Nav">
            <nav className="nav-container">
                <div className="gg">GG.</div>
                <ul className="nav-list">
                    <li className="nav-list-item" >
                        <Link style={linkStyle("/")} to="/">Home</Link>
                    </li>
                    <li className="nav-list-item">
                        <Link style={linkStyle("/predictions")} to="/predictions">Predictions</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default Nav;