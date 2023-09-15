import React from 'react';
import { NavLink } from 'react-router-dom';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
import UserAlbum from '../UserAlbum/UserAlbum';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

import "./Sidebar.css"

const Sidebar = () => {
    return (
        <div className="side-bar-container">
            <div className="top-of-side-bar">
                <img className="soundify-logo" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1694681368/SOUNDIFY_9_znffp4.png" />
                

            </div>
            <div className="remaining-side-bar-container">
                <div className="library-container">
                    <NavLink to="/song/all">
                        {/* <button>See your Songs</button> */}
                    </NavLink>
                </div>
                <div className="playlists-container">
                <div className='home-button-container'>
                    <Link exact to="/">
                        <div className="home-link">Home</div>
                    </Link>
                        <div className="search-link">Search</div>
                        <div className="library-link">Your Library</div>
                    </div>
                    <p className="landing-h1">Playlists</p>
                    <UserPlaylist />
                    <NavLink exact to="/playlist/new">
                        <button>Add a New Playlist</button>
                    </NavLink>
                    <p className="landing-h1">Albums</p>
                    <UserAlbum />
                    <NavLink exact to="/album/new">
                        <button>Create your Album</button>
                    </NavLink>
                </div>
            </div>
        </div>
    );
}

export default Sidebar;