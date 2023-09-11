import React from 'react'
import Sidebar from '../Sidebar/Sidebar'
import Playlist from '../Playlists/Playlists'
import "./landingpage.css"

const LandingPage = () => {
    return (
        <div className="landing-page-container">
            <Sidebar/>
            <div className="main-content-container">
                <div className="soundify-playlists-container">
                    <h1 className="landing-h1">Soundify Playlists</h1>
                    <div className="landing-page-playlists-container">
                        <Playlist/>
                    </div>
                </div>
                <div className="focus-container">
                    <h1 className="landing-h1">Focus</h1>
                </div>
            </div>
        </div>

    )
}

export default LandingPage