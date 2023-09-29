import React, { useEffect } from 'react';
import AudioPlayer from 'react-h5-audio-player';
import { usePlayer } from "../../context/AudioPlayerContext";
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css';

const Player = ({ src }) => {
    const { playSong } = usePlayer();

    useEffect(() => {
        playSong(src);
    }, [playSong, src]);

    const handlePlay = (e) => {
        console.log("Audio started playing");
    }

    return (
        <div className="audiobar-background">
            <AudioPlayer
                src={src}
                onPlay={handlePlay}
            />
        </div>
    );
}

export default Player;
