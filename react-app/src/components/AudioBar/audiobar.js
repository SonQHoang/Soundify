import React, { useContext, useRef, useEffect } from 'react';
import { AuthContext } from '../../context/AuthContext';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css';
import { SongContext } from '../../context/SongContext';

const Player = () => {
    const playerRef = useRef();
    const { isAuthenticated } = useContext(AuthContext);

    useEffect(() => {
        if (!isAuthenticated && playerRef.current && playerRef.current.audio.current) {
            playerRef.current.audio.current.pause();
        }
    }, [isAuthenticated]);

    const {
        isPlaying,
        play,
        pause,
        currentSong,
        // currentTime,
        setCurrentTime,
        songTitle,
        artistName,
        albumCover,
    } = useContext(SongContext);

    const handleListen = (e) => {
        setCurrentTime(e.target.currentTime);
    };
    const handlePlay = (e) => {
        play();
    };

    const handlePause = (e) => {
        pause();
    };

    return (
        isAuthenticated && currentSong ? (
            <div className="audio-bar-container">
                <div className="audio-bar-song-info">
                    <div className="audio-bar-album-cover">
                    {albumCover ? <img className="album-cover-image" src={albumCover} alt="Album Cover" /> : null}
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
        ) : null
    );
};

export default Player;
