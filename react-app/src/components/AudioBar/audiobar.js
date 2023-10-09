import React, { useContext, useRef, useEffect } from 'react';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css';
import { SongContext } from '../../context/SongContext';

const Player = () => {
    const playerRef = useRef();
    const { 
        isPlaying, play, pause, currentSong, setCurrentSong, 
        currentTime, setCurrentTime, songTitle, setSongTitle, 
        artistName, setArtistName 
    } = useContext(SongContext);

    console.log('What is the songTitle=====>', songTitle)
    const handleListen = (e) => {
        setCurrentTime(e.target.currentTime);
    };
    const handlePlay = (e) => {
        play();
    };

    const handlePause = (e) => {
        pause();
    };

    useEffect(() => {
        if (playerRef.current && playerRef.current.audio.current) {
            playerRef.current.audio.current.currentTime = currentTime;
        }
    }, [currentTime, currentSong]);

    return (
        <div className="audio-bar-container">
            <div className="audio-bar-song-info">
                <div>
                    Album Cover
                </div>
                <div>
                    <div>{songTitle}</div>
                    <div>{artistName}</div>
                </div>
            </div>
            <AudioPlayer
                ref={playerRef}
                autoPlayAfterSrcChange={false}
                src={currentSong}
                onPlay={handlePlay}
                onPause={handlePause}
                onListen={handleListen}
                autoPlay={isPlaying}
            />
        </div>
    );
};

export default Player;
