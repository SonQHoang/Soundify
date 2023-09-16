import React from 'react';
import { NavLink } from 'react-router-dom';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
import UserAlbum from '../UserAlbum/UserAlbum';


import "./Sidebar.css"

const Sidebar = () => {
    return (
        <div className="side-bar-container">
            <div className="top-of-side-bar">
                {/* <img className="soundify-logo" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1694681368/SOUNDIFY_9_znffp4.png" /> */}
                <div className='home-button-container'>
                    <div>
                        <NavLink exact to="/">
                            Home
                        </NavLink>
                    </div>
                    <div>
                        Search
                    </div>
                </div>
                <div className="library-container">
                    <div className="library-inner">
                        <div className="library-and-nav-buttons">
                            <div className="library-top">
                                <div>
                                    <button>Your library</button>
                                </div>
                                <div>
                                    <button>(Plus Icon - Add a playlist)</button>
                                </div>
                            </div>
                            <div className="library-bottom">
                                <div>
                                    <button>Playlists</button>
                                    <button>Artists</button>
                                    <button>Albums</button>
                                </div>
                            </div>
                            <div className="library-container">
                                <NavLink to="/song/all">
                                    {/* <button>See your Songs</button> */}
                                </NavLink>
                            </div>
                            <div className="playlists-container">
                                <p className="landing-h1"></p>
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
                </div>
            </div>
        </div>
    );
}

export default Sidebar;