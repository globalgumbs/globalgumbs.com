import React from 'react';
import './css/Projects.css';
import linkLogo from './assets/Link.png';

const Projects = () => {
    return (
        <div id="projects" className="Projects">
            <div className="headline">Projects</div>
            <div className="project-box">
                <div className="project-title">
                    <a href="/predictions">NBA Predictions </a>
                    <img src={linkLogo} alt="link" className="link-logo"/>
                </div>

                <div className="project-date">
                    2024
                </div>

                <div className="project-body">
                    I trained and deployed a machine learning model to predict the outcome of NBA games. 
                    The model is an artificial neural network and it is trained on 8 years (around 10,000 games) of NBA game data
                    to predict the outcome of games based on difference between each team's average stats within this season.
                    Within Python, I used Pandas to clean and preprocess the data, NumPy for numerical calculations, and PyTorch/Scikit Learn
                    to train and evaluate different models. I rewrote my personal website using ReactJS in order to update 
                    the predictions dynamically every day. The site is hosted on AWS Amplify and the model is deployed through
                    Github Actions.
                    <br /><br />
                    I plan to contine to improve the model by experimenting with different features and hyperparameters in an attempt to improve
                    the accuracy.
                </div>
            </div>
            <hr className="project-divider"/>

            <div className="project-box">
                <div className="project-title">
                    <a href="https://www.youtube-nocookie.com/embed/NSbPm0FY6Jg?si=V-2-nkJpTQ6S3w8s&amp;start=6925&autoplay=1&mute=1" target="_blank" rel="noreferrer">
                        Ball Beam Balance
                    </a>
                    <img src={linkLogo} alt="link" className="link-logo"/>
                </div>

                <div className="project-date">
                    2023
                </div>

                <div className="project-body">
                    For my senior capstone project, I worked in a group of 4 to design a Ball Beam Balance system, which would be used 
                    as a visual aid for teaching university level controls courses.
                    My group and I modeled components for our system using SOLIDWORKS and 3D printed several of them using
                    Ultimaker Cura. We programmed and calibrated the PID control system for the servo
                    motor, using input from an infrared sensor. Near the end of the semester, we presented our project to a group of UMBC professors and industry professionals.
                </div>
            </div>
            <hr className="project-divider"/>

            <div className="project-box">
                <div className="project-title">
                    <a href="/">
                        globalgumbs.com
                    </a>
                    <img src={linkLogo} alt="link" className="link-logo"/>
                </div>

                <div className="project-date">
                    2023
                </div>

                <div className="project-body">
                    In 2023, I built this page as a static website using HTML and CSS and hosted it
                    using AWS Amplify. I ended up rewriting the site using ReactJS in 2024.
                </div>
            </div>
            <hr className="project-divider"/>
            <div className="project-box">
                <div className="project-title">
                    <a href="https://x.com/THIRTYPIECE" target="_blank" rel="noreferrer">
                        @THIRTYPIECE
                    </a>
                    <img src={linkLogo} alt="link" className="link-logo"/>
                </div>

                <div className="project-date">
                    2021
                </div>
            

                <div className="project-body">
                    In early 2021, I built a NBA highlight compiler and editor with Ruby called ThirtyPiece.
                    The program uses HTTP requests to compile stats for all NBA games from a selected date from nba.com, and identifies players who scored 30 or more points that night.
                    For each player that scored 30 or higher, a highlight reel for that games is created by compiliing footage for each basket made and stitching it together,
                    using open-source CLI based software FFmpeg. I used the Twitter API to programmatically tweet each player's highlight tape with a customized caption to make the videos searchable and increase view count.
                </div>
            </div>
            <hr className="project-divider"/>
            <div className="project-box">
                <div className="project-title">
                    Walmart ACO
                </div>

                <div className="project-date">
                    2021
                </div>

                <div className="project-body">
                    I created and iterated on a program to monitor the Walmart online product database and complete a
                    purchase of in-demand items in 3-5 seconds after the item becomes available. I built the first version
                    of this program in response to the scarcity of certain items in my community due to the COVID-19 pandemic.
                    There was an extremely high demand for products that people could use to safely interact with friends
                    and family outdoors, while still following the social distancing guidelines. I used Selenium based Ruby plugin Watir
                    to build a program that would constantly monitor the site for a specified product, and immediately checkout when the
                    product restocked. I had some success with this method, but after capturing the relevant API calls, I later changed the method to use Ruby's HTTP request module to monitor
                    the product page and post the neccesary shipping and billing information. This drastically inreased the speed and success rate
                    of the program, leading to a product restock to checkout time of 3-5 seconds.
                </div>
            </div>
        </div>
    );
};

export default Projects;
