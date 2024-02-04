import React, { useContext, useRef, useEffect } from 'react';
import { AuthContext } from '../../context/AuthContext';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './audiobar.css';
import { SongContext } from '../../context/SongContext';

const Player = () => {
    const playerRef = useRef(); // useRef persistently stores a mutable value that DOESN'T cause a re-render. Think of a "box" holding a mutable (Can be modified) value
                                // All ref objects have a property called .current. If you don't provide useRef with an arg, .current is undefined UNTIL the component its attached to mounts.
    const { isAuthenticated } = useContext(AuthContext); // Using context to gain access to isAuth from AuthContext to determine if audio player should be rendered

    useEffect(() => {
        // if user is NOT authenicated && if playerRef has mounted && audio is there
        if (!isAuthenticated && playerRef.current && playerRef.current.audio.current) {
            playerRef.current.audio.current.pause(); // If the above are all true, then the song can be paused.
        }
    }, [isAuthenticated]); // Dependency array is waiting to see if isAuth changes. If the user logs out, it will become false, the effect will run and pause the audio (If it's playing). If it stays true nothing will change. (Audio is not playing)

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
        // playerRef.current will be the instance of the AudioPlayer once the component mounts
        // audio.current holds the value of the actual audio element
        if (audioElement) {
            if (isPlaying) { 
                audioElement.play(); // if isPlaying is truthy, audio will play
            } else {
                audioElement.pause(); // else audio will pause
            }
        }
    }, [isPlaying]);

    return ( // Rendering...
        isAuthenticated && currentSong ? ( // if user is logged in and currentSong is truthy
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
                    ref={playerRef} // This allows us to access the instance of the AudioPlayer component throughout the component by setting playerRef's .current property to the mounted instance of AudioPlayer
                                    // As a result, once AudioPlayer mounts, we can access any properties or methods that are exposed by the instance
                                    // We're able to continually hold ont this value across renders without causing a re-render
                    autoPlayAfterSrcChange={false}
                    src={currentSong} // CurrentSong that is playing
                    onPlay={play} // Controls play (From Song context)
                    onPause={pause} // Controls pause (From Song Context)
                    listenInterval={100}
                    autoPlay={isPlaying} // Audio will start playing automatically if isPlaying === True
                    showSkipControls={true} //Enables skip controls to be visible
                    showJumpControls={true} // Enables jump controls to be visible
                    onClickNext={() => handleNextTrack(songs)} // Next button functionality
                    onClickPrevious={() => handlePreviousTrack(songs)} // Previosu button funtionality
                />
            </div>
        ) : null
    );
};

export default Player;
