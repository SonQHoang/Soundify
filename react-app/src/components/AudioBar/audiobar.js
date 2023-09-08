import React from 'react'
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';

const Player = ({src}) => {
    // console.log('Player component =======>', src)

    return (
        <AudioPlayer
            autoPlay
            src={src}
            onPlay={e => console.log("onPlay")}
        />
    )
}

export default Player