import React from 'react'
import Sidebar from '../Sidebar/Sidebar'
// import Playlist from '../Playlists/Playlists'
import Header from '../Header/Header'
import UserPlaylist from '../UserPlaylist/UserPlaylist'
import Footer from '../Footer/Footer'
import "./landingpage.css"

const LandingPage = () => {
    return (
        <div className="landing-page-container">
            <Sidebar/>
            <div className="main-content-container">
                <div className="soundify-playlists-container">
                <Header/>
                    <h1 className="landing-h1">Soundify Playlists</h1>
                    <div className="landing-page-playlists-container">
                        <UserPlaylist/>
                    </div>
                </div>
                <div className="focus-container">
                    <h1 className="landing-h1">Focus</h1>
                </div>
                <Footer/>
            </div>
        </div>

    )
}

export default LandingPage