import React, {useEffect } from "react";
import { useParams } from "react-router-dom"
import { useSelector, useDispatch } from "react-redux";
import TestSideBar from "../TestComponents/TestSideBar";
import TestNav from "../TestComponents/TestNav";
// import { SongContext } from "../../context/SongContext";
import { getSingleSong } from "../../store/songs";
import "./SongDetails.css"

function SongDetails() {
    const { songId } = useParams()
    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    // const userId = sessionUser.id

    const currentSong = Object.values(useSelector(state => state.songs.singleSong))

    useEffect(() => {
        dispatch(getSingleSong(songId))
    }, [songId])

    return (
        <>
            <div className="page-container">
                <TestSideBar />
                <div className="main-content-container">
                    <div className="main-content-nav-container">
                        <TestNav />
                    </div>
                    <div className="main-content">
                        <div className="Song-image-and-title-container">
                            <div className="Song-image-container">
                                {/* <img className='Song-image' src={currentSong}></img> */}
                            </div>
                            <div className="Song-information-container">
                                <div className="Song-Song-title-container">
                                    <p>Song</p>
                                    <h1>{currentSong?.title}</h1>
                                </div>
                                <div className="song-user-details">
                                    <img className="song-user-picture" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png"></img>
                                </div>
                                <div className="song-songs-container">
                                    {(currentSong)?.map((song, index) => (
                                        <div key={index} className="individual-song-songs">
                                            <div className="song-lyrics">{song.lyrics}</div>
                                        </div>
                                    ))}

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default SongDetails;
