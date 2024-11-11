import React from 'react';
import './css/Home.css';
import githubIcon from './assets/Github.png';
import emailIcon from './assets/Email.svg';
import linkedinIcon from './assets/LinkedIn.png';
import downArrow from './assets/down.png';
import pfp from './assets/pfp.png';
import Projects from './Projects';

function Home() {
    return (
        <div className="Home">
            <div className="About">
                <div className="headline">
                    Albert K. Gumbs
                </div>
                
                <img className="profile" src={pfp} alt="headshot"></img>
                <div className="blurb">
                    As a Systems Engineer, I currently support an evolutionary US Navy
                    Electro-Optic / Infrared (EO/IR) sensor system acquisition program.
                    I graduated from UMBC with a Bachelor of Science in Mechanical Engineering in 2023, 
                    and I'll be beginning my Masters program in Computer Science at Georgia Tech in January 2025.
                    My professional interests are in robotics and other applications of algorithms to real world problems.
                </div>
                    
                <hr className="divider" />

                <div className="social-bar">
                    <a className="socialLink" href="https://www.linkedin.com/in/albertgumbs" target="_blank" rel="noreferrer">
                        <img className="social" src={linkedinIcon} alt="LinkedIn" />
                    </a>
                    <a className="socialLink" href="mailto:albertgumbs38@gmail.com" target="_blank" rel="noreferrer">
                        <img className="email" src={emailIcon} alt="Email"/>
                    </a>
                    <a className="socialLink" href="https://www.github.com/globalgumbs" target="_blank" rel="noreferrer">
                        <img className="social" src={githubIcon} alt="Github" />
                    </a>
                </div>
                <a href="#projects" className="arrowLink">
                    <img className="arrow" src={downArrow} alt="arrow" />
                </a>
            </div>
            <Projects />
        </div>          
    );
}

export default Home;
