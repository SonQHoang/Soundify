import React from 'react';
import { NavLink } from 'react-router-dom';

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
                <button>Add a New Playlist</button>
            </div>
            <div className="library-container">
                <h1 className="landing-h1">Your Library</h1>
            </div>
        </div>
    );
}

export default Sidebar;