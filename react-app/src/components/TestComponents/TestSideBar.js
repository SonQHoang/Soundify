import React, { useState } from 'react';
import { NavLink } from 'react-router-dom'
import './TestSideBar.css';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
import UserAlbum from '../UserAlbum/UserAlbum';


const TestSideBar = () => {

    const [dropDownMenu, setDropDownMenu] = useState(false)

    const handleDropDown = () => {
        setDropDownMenu(!dropDownMenu)
    }

    return (
        <>
            <div className="side-bar-container">
                <div className="home-button-container">
                    <div className="home-button-top">
                        <div className="home-icon-container">
                            <img className="home-icon" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695021959/home-5-16_fne9qv.png"></img>
                        </div>
                        <div className="home-text-container">
                            <NavLink exact to="/landing-page">
                                <p>Home</p>
                            </NavLink>
                        </div>
                    </div>
                    <div className="home-button-bottom">
                        <div className="search-icon-container">
                            <img className="search-icon" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695021955/search-3-16_lcobap.png"></img>
                        </div>
                        <div>
                            <p>Search</p>
                        </div>
                    </div>
                </div>
                <div className="playlist-albums-container">
                    <div className="library-create-playlist-container">
                        <div className="library-create-upper">
                            <h2>Your Library</h2>
                                <button className="create-playlist-button" onClick={handleDropDown}>
                                    <img src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1694920890/icons8-plus-16_2_w7ebvj.png" alt="Create Playlist" />
                                </button>
                            {dropDownMenu && (
                                <div className="dropdown-menu">
                                    <div>
                                        <NavLink exact to="/playlist/new">
                                            <button onClick={() => {}}>
                                                Create Playlist
                                            </button>
                                            </NavLink>
                                        <NavLink exact to="/album/new">
                                            <button onClick={() => {}}>
                                                Create Album
                                            </button>
                                            </NavLink>
                                    </div>
                                </div>
                            )}
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