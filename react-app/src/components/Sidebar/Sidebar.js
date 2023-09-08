import React from 'react';
import { NavLink } from 'react-router-dom';
import Songs from '../Songs/songs';
import Playlist from '../Playlists/Playlists';
import "./Sidebar.css"

const Sidebar = () => {
    return (
        <div className="side-bar-container">
            <div className='home-button-container'>
                <NavLink exact to="/">
                    Home
                </NavLink>
            </div>
            <div className="playlists-container">
                <h1 className="landing-h1">Playlists</h1>
                <Playlist/>
                <NavLink exact to="/playlist/new">
                    <button>Add a New Playlist</button>
                </NavLink>
            </div>
            <div className="library-container">
                <h1 className="landing-h1">Your Library</h1>
                <Songs/>
            </div>
        </div>
    );
}

export default Sidebar;