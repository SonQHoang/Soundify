import React from 'react'
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/src/styles.scss'
// import './custom-audio-player.css';

const Player = () => {
    return (
        <AudioPlayer
            autoPlay
            src="http://"
            onPlay={e => console.log("onPlay")}
        />
    )
}

export default Player