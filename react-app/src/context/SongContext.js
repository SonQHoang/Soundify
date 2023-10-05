import React, { createContext, useState } from 'react';

export const SongContext = createContext();

export const SongProvider = ({ children }) => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentSong, setCurrentSong] = useState(null);
    const [currentTime, setCurrentTime] = useState(0);

    const play = () => setIsPlaying(true);
    const pause = () => setIsPlaying(false);

    return (
        <SongContext.Provider value={{ isPlaying, play, pause, currentSong, setCurrentSong, currentTime, setCurrentTime }}>
            {children}
        </SongContext.Provider>
    );
};
