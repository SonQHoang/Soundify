import { useContext, useState, createContext } from "react";

const AudioPlayerContext = createContext();

export function usePlayer() {
    return useContext(AudioPlayerContext);
}

export function PlayerProvider({ children }) {
    const [currentSong, setCurrentSong] = useState(null);

    const playSong = (audio_url) => {
        setCurrentSong(audio_url);
    };

    const pauseSong = () => {
        setCurrentSong(null);
    };

    return (
        <AudioPlayerContext.Provider value={{ currentSong, playSong, pauseSong }}>
            {children}
        </AudioPlayerContext.Provider>
    );
}