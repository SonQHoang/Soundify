import React from 'react'
import TestSideBar from '../TestComponents/TestSideBar'
import TestNav from '../TestComponents/TestNav'
import UserPlaylistTile from '../UserPlaylistTile/UserPlaylistTile'
import UserAlbumTile from '../UserAlbumTile/UserAlbumTile'
import Player from '../AudioBar/audiobar'
import Footer from '../Footer/Footer'
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
                                <h2>Your Playlists</h2>
                                <div className="playlist-list">
                                    <UserPlaylistTile />
                                </div>
                            </div>
                        </div>

                        <div className="personalized-albums">
                            <h2>Your Albums</h2>
                            <ul className="albums-list">
                                <UserAlbumTile />
                            </ul>
                        </div>
                        <div className="general-content">
                            {/* <h4>General Content</h4>
                            <ul className="generalized-list">
                                <li>This is Love</li>
                                <li>This is Pop</li>
                                <li>This is Worship</li>
                                <li>This is Instrumental</li>
                            </ul> */}
                        </div>
                    </div>
                </div>
            </div>
            {/* <Footer/> */}
        </>
    )
}

export default MainPage