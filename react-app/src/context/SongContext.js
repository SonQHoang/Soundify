import React, { createContext, useState } from 'react';

export const SongContext = createContext();

export const SongProvider = ({ children }) => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentSong, setCurrentSong] = useState(null);
    const [currentTime, setCurrentTime] = useState(0);
    const [songTitle, setSongTitle] = useState(null);
    const [artistName, setArtistName] = useState(null);

    const play = () => setIsPlaying(true);
    const pause = () => setIsPlaying(false);

    return (
        <SongContext.Provider value={{
            isPlaying,
            play,
            pause,
            currentSong,
            setCurrentSong,
            currentTime,
            setCurrentTime,
            songTitle, 
            setSongTitle, 
            artistName, 
            setArtistName
            }}>
            {children}
        </SongContext.Provider>
    );
};
