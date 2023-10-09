import React, { useState } from 'react';
import { NavLink } from 'react-router-dom'
import './TestSideBar.css';
import UserPlaylist from '../UserPlaylist/UserPlaylist';
import UserAlbum from '../UserAlbum/UserAlbum';


const TestSideBar = () => {

    const [dropDownMenu, setDropDownMenu] = useState(false)
    const [activeLink, setActiveLink] = useState('playlists')


    const handleDropDown = () => {
        setDropDownMenu(!dropDownMenu)
    }

    const handleFeatureClick = () => {
        alert("This feature will be added in the future. Check back again soon!")
    }

    return (
        <>
            <div className="side-bar-container">
                <div className="home-button-container">
                    <div className="home-button-top">
                        <div className="home-icon-container">
                            <img className="home-icon" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695245412/House_Icon_zztfmg.png"></img>
                        </div>
                        <div className="home-text-container">
                            <NavLink exact to="/landing-page">
                                <p>Home</p>
                            </NavLink>
                        </div>
                    </div>
                    <div className="home-button-bottom">
                        <div className="search-icon-container">
                            <img className="search-icon" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695240816/00FFFFFF_b3eppw.png"></img>
                        </div>
                        <div>
                            <button onClick={handleFeatureClick}>Search</button>
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
                                            <button onClick={() => { }}>
                                                Create Playlist
                                            </button>
                                        </NavLink>
                                        <NavLink exact to="/album/new">
                                            <button onClick={() => { }}>
                                                Create Album
                                            </button>
                                        </NavLink>
                                    </div>
                                </div>
                            )}
                        </div>
                        <div className='library-create-lower'>
                            <button onClick={() => setActiveLink('playlists')} className={activeLink === 'playlists' ? 'active' : ''}>Playlists</button>
                            <button onClick={() => setActiveLink('albums')} className={activeLink === 'albums' ? 'active' : ''}>Albums</button>
                            <button onClick={handleFeatureClick}>Artists</button>
                        </div>
                    </div>
                    {activeLink === 'playlists' && (
                        <div className='create-playlist'>
                            {/* <h2>Playlists</h2> */}
                            <ul className="playlist-list-container">
                                <UserPlaylist />
                            </ul>
                        </div>
                    )}
                    {activeLink === 'albums' && (
                        <div className="albums-container">
                            {/* <h2>Albums</h2> */}
                            <div className="create-albums-button-container">
                                <ul>
                                    <UserAlbum />
                                </ul>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </>
    )
}

export default TestSideBar