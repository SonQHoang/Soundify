import React, { useState, useRef, useContext, useEffect } from 'react'
import './TestFooter.css'

const TestFooter = () => {
    // const [play, setPlay] = useState(false);
    const [currentTime, setCurrentTime] = useState(0)
    const [duration, setDuration] = useState(0)
    const [volume, setVolume] = useState(1)
    const [repeat, setRepeat] = useState(false)
    const [shuffle, setShuffle] = useState(false)
    const audioRef = useRef()
    // const randomIndex = Math.floor(Math.random() * (contextSongList.length - 0) + 0)


    return (
        <div>
            <audio
                ref={audioRef}
            />

            <div id='media-player-song-info-container'>
                <img id='media-player-album-art' ></img>
                <div id='media-player-song-info'>
                    <h2 id='media-player-song-name'></h2>
                    <p id='media-player-artist-name'></p>
                </div>
            </div>

            <div id='media-player-controls-container'>
                <div id='media-player-controls'>
                    <button className={shuffle ? 'shuffle-button active' : 'shuffle-button'}> <i class="fa-solid fa-shuffle"></i> </button>

                    <button id='step-back-button' > <i class="fa-solid fa-backward-step"></i> </button>

                    {!audioRef.current?.paused && <button className='media-player-play-button' > <i class="fa-solid fa-circle-pause"></i> </button>}

                    {audioRef.current?.paused && <button className='media-player-play-button' > <i class="fa-solid fa-circle-play"></i> </button>}

                    <button id='step-forward-button' > <i class="fa-solid fa-forward-step"></i> </button>

                    <button className={repeat ? 'repeat-button active' : 'repeat-button'} > <i class="fa-solid fa-repeat"></i> </button>
                </div>

                <div id='volume-controls-container'>


                </div>
            </div>

            <div id='song-volume-bar-container'>
                <div id='song-volume-bar'>

                </div>
            </div>

        </div >
    )
}

export default TestFooter