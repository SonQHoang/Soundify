import React from 'react';
import { NavLink } from 'react-router-dom'
import './TestSideBar.css';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
import UserAlbum from '../UserAlbum/UserAlbum';

const TestSideBar = () => {


    return (
        <>
            <div className="side-bar-container">
                <ul className="home-button-container">
                    <div>
                        <NavLink exact to="/test">
                            <p>Home</p>
                        </NavLink>
                        <p>Search - Add a pop up saying 'Coming Soon!'</p>
                    </div>
                </ul>
                <div className="playlist-albums-container">
                    <div className="library-create-playlist-container">
                        <div className="library-create-upper">
                            <h2>Your Library</h2>
                        <NavLink exact to="/playlist/new">
                            <button className="create-playlist-button">
                                <img src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1694920890/icons8-plus-16_2_w7ebvj.png" alt="Create Playlist" />
                            </button>
                        </NavLink>
                        </div>
                        <div className='library-create-lower'>
                            <button>Playlists</button>
                            <button>Artists</button>
                            <button>Albums</button>
                        </div>
                    </div>
                    <div className='create-playlist'>
                        <h2>Playlists</h2>
                        <ul className="playlist-list-container">
                            <UserPlaylist />
                        </ul>
                    </div>
                    <div className="albums-container">
                        <h2>Albums</h2>
                        <div className="create-albums-button-container">
                            <ul>
                                <UserAlbum />
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default TestSideBar