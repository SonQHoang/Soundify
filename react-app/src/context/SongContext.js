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
    const [currentView, setCurrentView] = useState('playlist');
    
    const playlistSongs = useSelector(state => state.playlist.singlePlaylist.songs);
    const albumSongs = useSelector(state => state.album.singleAlbum.songs)

    const songs = currentView === 'playlist' ? playlistSongs : albumSongs;

    const setCurrentSong = (song) => {
        setCurrentTime(0);
        _setCurrentSong(song);
    };

    const play = () => {
        setIsPlaying(true);
    };
    
    const pause = () => {
        setIsPlaying(false);
    };

    const togglePlay = () => {
        setIsPlaying((prev) => !prev);
    };
    
    const playFromStart = () => {
        if (firstPlay && songs && songs.length > 0) {
            setCurrentSong(songs[0].audio_url);
            setSongTitle(songs[0].title);
            setArtistName(songs[0].artist);
            setAlbumCover(songs[0].album_arts);
            setFirstPlay(false);
            play();
        } else {
            togglePlay();
        }
    };

    return (
        <SongContext.Provider value={{
            play,
            pause,
            currentSong,
            setCurrentSong,
            currentTime,
            setCurrentTime,
            songTitle,
            setSongTitle,
            isPlaying,
            setIsPlaying,
            artistName,
            setArtistName,
            albumCover,
            setAlbumCover,
            togglePlay,
            playFromStart,
            setFirstPlay,
            currentView,
            setCurrentView
        }}>
            {children}
        </SongContext.Provider>
    );
};
