import { React } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './css/Nav.css';

function Nav() {
    const location = useLocation();

    const linkStyle = (path) => ({
        textDecoration: location.pathname === path ? 'underline' : 'none',
        color: location.pathname === path ? 'rgb(129, 167, 177)' : 'black',
    });

    return (
        <div className="Nav">
            <nav className="nav-container">
                <ul className="nav-list">
                    <li className="nav-list-item left" >
                        <Link className="link" style={linkStyle("/")} to="/">Home</Link>
                    </li>
                    <li className="nav-list-item right">
                        <Link className="link" style={linkStyle("/predictions")} to="/predictions">NBA Predictions</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default Nav;