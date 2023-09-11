import React from 'react'
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';

const Player = ({src}) => {
    console.log('Player component =======>', src)

    const handlePlay = (e) => {
        console.log("Audio started playing")
    }
    return (
        <AudioPlayer
            autoPlay
            src={src}
            onPlay={handlePlay}
        />
    )
}

export default Player