import React from 'react';
import './css/Home.css';
import gh from './assets/Github.png';
import ig from './assets/Instagram.png';
import li from './assets/LinkedIn.png';

function Home() {
    return (
        <div className="Home">
            <div className="headline">
                Albert K. Gumbs
            </div>

            <div className="sub-headline">
                <br />Hi! Welcome to my site. I'm currently working as a Systems Engineer supporting an evolutionary Navy
                Electro-Optic / Infrared (EO/IR) sensor system acquisition program.
                I graduated from UMBC with a BS in Mechanical Engineering in 2023.
                My professional interests are in the intersection of mechanical and software engineering.
            </div>

            <hr />

            <div className="social-bar">
                <a href="https://www.linkedin.com/in/albertgumbs" target="_blank">
                    <img className="social" src={li} alt="LinkedIn" />
                </a>
                <a href="https://www.instagram.com/globalgumbs" target="_blank">
                    <img className="social" src={ig} alt="Instagram" />
                </a>
                <a href="https://www.github.com/globalgumbs" target="_blank">
                    <img className="social" src={gh} alt="Github" />
                </a>
            </div>
        </div>          
    );
}

export default Home;
