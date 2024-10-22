import React from 'react';
import './css/Projects.css';

const Projects = () => {
    return (
        <div className="Projects">
            <link rel="stylesheet" media="only screen and (min-width: 768px)" href="./css/Projects.css" />
            <link rel="stylesheet" media="only screen and (max-width: 767px)" href="./css/Projects-Mobile.css" />
            <link href="https://fonts.googleapis.com/css2?family=Lato" rel="stylesheet" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />

            <div>
                <div className="headline">
                    Projects.
                </div>

                <div className="project-box">
                    <div className="project-title">
                        UMBC Mechanical Engineering Capstone Project
                    </div>

                    <div className="project-date">
                        January - May 2023
                    </div>

                    <div className="project-body">
                        For my senior capstone project, I worked in a group of 4 to design a Ball Beam Balance system, which would be used 
                        as a visual aid for teaching university level controls courses.
                        My group and I modeled components for our system using SOLIDWORKS and 3D printed several of them using
                        Ultimaker Cura. During this project, I was personally responsible for programming and calibrating the PID control system for the servo
                        motor, using input from an infrared sensor. Near the end of the semester, we presented our project to a group of UMBC professors and industry professionals.
                    </div>

                    <iframe className="yt-video" src="https://www.youtube-nocookie.com/embed/NSbPm0FY6Jg?si=V-2-nkJpTQ6S3w8s&amp;start=6925&autoplay=1&mute=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
                </div>
                <hr />
                <div className="project-box">
                    <div className="project-title">
                        GlobalGumbs.com
                    </div>

                    <div className="project-date">
                        August 2023
                    </div>

                    <div className="project-body">
                        As a way to exercise my programming muscles, I decided to 
                        build this website from scratch. I used HTML and CSS and hosted
                        the site using AWS. I plan to continue adding features in the future.
                    </div>
                </div>
                <hr />
                <div className="project-box">
                    <div className="project-title">
                        @THIRTYPIECE
                    </div>

                    <div className="project-date">
                        March 2021
                    </div>
                

                    <div className="project-body">
                        In early 2021, I built a NBA highlight compiler and editor with Ruby called <a href="https://twitter.com/i/flow/login?redirect_after_login=%2FTHIRTYPIECE" target="_blank"><u>@THIRTYPIECE</u></a>.
                        The program uses HTTP requests to compile stats for all NBA games from nba.com, and identifies players who scored 30 or more points that night.
                        For each player that scored 30 or higher, a highlight reel for that games is created by compiliing footage for each basket made and stitching it together,
                        using open-source CLI based software FFmpeg. I used the Twitter API to programmatically tweet each player's highlight tape with a customized caption to make the videos searchable and increase view count.
                    </div>
                </div>
                <hr />
                <div className="project-box">
                    <div className="project-title">
                        Walmart Auto-Checkout
                    </div>

                    <div className="project-date">
                        January 2021
                    </div>

                    <div className="project-body">
                        I created and iterated on a program to monitor the Walmart online product database and complete a
                        purchase of in-demand items in 3-5 seconds after the item becomes available. I built the first version
                        of this program in response to the scarcity of certain items in my community due to the COVID-19 pandemic.
                        There was an extremely high demand for certain products that people could use to safely interact with friends
                        and family outdoors, while still following the social distancing guidelines. I used Selenium based Ruby plugin Watir
                        to build a program that would constantly monitor the site for a specified product, and immediately checkout when the
                        product restocked. I had some success with this method, but I later changed the method to use HTTP requests to monitor
                        the product page and send the neccesary shipping and billing information. This drastically inreased the speed and success rate
                        of the program, leading to a product restock to checkout time of 3-5 seconds.
                    </div>
                </div>
                <div className="spacer"></div>
            </div>
        </div>

    );
};

export default Projects;
