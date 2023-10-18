import React, { createContext, useState } from 'react';
import { useSelector } from 'react-redux';

export const SongContext = createContext();

export const SongProvider = ({ children }) => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentSong, _setCurrentSong] = useState(null);
    const [currentTime, setCurrentTime] = useState(0);
    const [songTitle, setSongTitle] = useState(null);
    const [artistName, setArtistName] = useState(null);
    const [albumCover, setAlbumCover] = useState(null);
    const [firstPlay, setFirstPlay] = useState(true);
    
    const playlistSongs = useSelector(state => state.playlist.singlePlaylist.songs);

    const setCurrentSong = (song) => {
        setCurrentTime(0);
        _setCurrentSong(song);
    };

    const play = () => setIsPlaying(true);
    const pause = () => setIsPlaying(false);

    const togglePlay = () => {
        setIsPlaying((prev) => !prev);
    };
    
    const playFromStart = () => {
        if (firstPlay && playlistSongs && playlistSongs.length > 0) {
            setCurrentSong(playlistSongs[0].audio_url);
            setSongTitle(playlistSongs[0].title);
            setArtistName(playlistSongs[0].artist);
            setAlbumCover(playlistSongs[0].album_arts);
            setFirstPlay(false);
            play();
        } else {
            togglePlay();
        }
    };

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
            setArtistName,
            albumCover,
            setAlbumCover,
            togglePlay,
            playFromStart,
            setFirstPlay
        }}>
            {children}
        </SongContext.Provider>
    );
};
