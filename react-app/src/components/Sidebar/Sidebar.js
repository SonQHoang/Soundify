import React from 'react';
import { NavLink } from 'react-router-dom';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
// import Song from '../Songs/Song';
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
                <p className="landing-h1">Playlists</p>
                <UserPlaylist />
                <NavLink exact to="/playlist/new">
                    <button>Add a New Playlist</button>
                </NavLink>
            </div>
            <div className="library-container">
                <h1 className="landing-h1">Your Library</h1>
                    <NavLink to="/song/all">
                        <button>See your Songs</button>
                    </NavLink>
            </div>
        </div>
    );
}

export default Sidebar;