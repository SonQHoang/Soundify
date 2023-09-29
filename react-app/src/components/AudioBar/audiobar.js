import React from 'react'
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css'

const Player = ({src}) => {

    const handlePlay = (e) => {
        console.log("Audio started playing")
    }
    return (
        <div className="audiobar-background">
            <AudioPlayer
                autoPlay
                src={src}
                onPlay={handlePlay}
            />
        </div>
    )
}

export default Player