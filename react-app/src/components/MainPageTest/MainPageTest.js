import React from 'react'
import TestSideBar from '../TestComponents/TestSideBar'
import TestNav from '../TestComponents/TestNav'
import UserPlaylistTile from '../UserPlaylistTile/UserPlaylistTile'
import UserAlbumTile from '../UserAlbumTile/UserAlbumTile'
import "./MainPageTest.css"

const MainPage = () => {
    return (
        <>
            <div className="page-container">
                <TestSideBar />
                <div className="main-content-container">
                    <div className="main-content-nav-container">
                        <TestNav />
                    </div>
                    <div className="main-content">
                        <div className="personalized-content-container">
                            <div className="personalized-playlist">
                                <h2>Playlists</h2>
                                <div className="playlist-list">
                                    <UserPlaylistTile />
                                </div>
                            </div>
                        </div>

                        <div className="personalized-albums">
                            <h2>Albums</h2>
                            <ul className="albums-list">
                                <UserAlbumTile />
                            </ul>
                        </div>
                        <div className="general-content">
                        </div>
                    </div>
                </div>
            </div>
            
        </>
    )
}

export default MainPage