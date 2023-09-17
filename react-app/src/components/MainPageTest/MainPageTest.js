import React from 'react'
import TestSideBar from '../TestComponents/TestSideBar'
import TestNav from '../TestComponents/TestNav'
import TestFooter from '../TestComponents/TestFooter'
import UserPlaylistTile from '../UserPlaylistTile/UserPlaylistTile'
import "./MainPageTest.css"

const MainPageTest = () => {
    return (
        <>
            <div className="page-container">
                <TestSideBar/>
                <div className="main-content-container">
                    <div className="main-content-nav-container">
                        <TestNav/>
                    </div>
                    <div className="main-content">
                        <h2>This is where all of my tiles will go</h2>
                        <div className="personalized-content-container">
                            <div className="personalized-playlist">
                                <h4>Personalized Playlist</h4>
                                <div className="playlist-list">
                                    <UserPlaylistTile/>
                                    {/* <li>Playlist 1</li>
                                    <li>Playlist 2</li>
                                    <li>Playlist 3</li>
                                    <li>Playlist 4</li> */}
                                </div>
                            </div>
                            <div className="personalized-albums">
                                <h4>Personalized Albums</h4>
                                <ul className="albums-list">
                                    <li>Album 1</li>
                                    <li>Album 2</li>
                                    <li>Album 3</li>
                                    <li>Album 4</li>
                                </ul>
                            </div>
                            <div className="general-content">
                                <h4>General Content</h4>
                                <ul className="generalized-list">
                                    <li>This is Love</li>
                                    <li>This is Pop</li>
                                    <li>This is Worship</li>
                                    <li>This is Instrumental</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                {/* <TestFooter/> */}
            </div>
        </>
    )
}

export default MainPageTest