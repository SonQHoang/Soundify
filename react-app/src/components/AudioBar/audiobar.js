import React, { useContext, useRef, useEffect } from 'react';
import { AuthContext } from '../../context/AuthContext';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css';
import { SongContext } from '../../context/SongContext';

const Player = () => {
    const playerRef = useRef();
    const { isAuthenticated } = useContext(AuthContext); // Using context to gain access to isAuth from AuthContext to determine if audio player should be rendered

    useEffect(() => {
        if (!isAuthenticated && playerRef.current && playerRef.current.audio.current) {
            playerRef.current.audio.current.pause();
        }
    }, [isAuthenticated]);

    const {
        isPlaying,
        play,
        pause,
        togglePlay,
        currentSong,
        songs,
        setCurrentTime,
        songTitle,
        artistName,
        albumCover,
        handleNextTrack,
        handlePreviousTrack
    } = useContext(SongContext);
    

    useEffect(() => {
        const audioElement = playerRef.current?.audio.current;
        if (audioElement) {
            if (isPlaying) {
                audioElement.play();
            } else {
                audioElement.pause();
            }
        }
    }, [isPlaying]);

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
                    onPlay={play} 
                    onPause={pause} 
                    listenInterval={100}
                    autoPlay={isPlaying}
                    showSkipControls={true}
                    showJumpControls={true}
                    onClickNext={() => handleNextTrack(songs)}
                    onClickPrevious={() => handlePreviousTrack(songs)}
                />
            </div>
        ) : null
    );
};

export default Player;
