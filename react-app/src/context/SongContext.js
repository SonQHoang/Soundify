import React, { createContext, useState } from 'react';
import { useSelector } from 'react-redux';

export const SongContext = createContext(); // providing SongContext to be used by other components to access and manipulate music state w/o rneeidng to prop drill

export const SongProvider = ({ children }) => { // Provider; Wraps children components allowing them to have access to all of the following
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentSong, _setCurrentSong] = useState(null);
    const [currentTime, setCurrentTime] = useState(0);
    const [songTitle, setSongTitle] = useState(null);
    const [artistName, setArtistName] = useState(null);
    const [albumCover, setAlbumCover] = useState(null);
    const [firstPlay, setFirstPlay] = useState(true);
    const [currentView, setCurrentView] = useState('playlist');
    const [currentlyPlayingSongIndex, setCurrentlyPlayingSongIndex] = useState(null);
    const [currentTrackIndex, setCurrentTrackIndex] = useState(0);

    const handleNextTrack = (songList) => { // Controls skip forward
        const nextTrackIndex = (currentlyPlayingSongIndex + 1) % songList.length;
        setCurrentlyPlayingSongIndex(nextTrackIndex);
        setCurrentSong(songList[nextTrackIndex].audio_url);
        setSongTitle(songList[nextTrackIndex].title);
        setArtistName(songList[nextTrackIndex].artist);
        setAlbumCover(songList[nextTrackIndex].album_arts[0]);
    };
    
    const handlePreviousTrack = (songList) => { // Controls skip back
        const prevTrackIndex = (currentlyPlayingSongIndex - 1 + songList.length) % songList.length;
        setCurrentlyPlayingSongIndex(prevTrackIndex);
        setCurrentSong(songList[prevTrackIndex].audio_url);
        setSongTitle(songList[prevTrackIndex].title);
        setArtistName(songList[prevTrackIndex].artist);
        setAlbumCover(songList[prevTrackIndex].album_arts[0]);
    };

    const playlistSongs = useSelector(state => state.playlist.singlePlaylist.songs);
    const albumSongs = useSelector(state => state.album.singleAlbum.songs)

    const updateCurrentView = (view) => {
        setCurrentView(view);
    };


    const songs = currentView === 'playlist' ? playlistSongs : albumSongs; // View swapper for playlists

    const setCurrentSong = (song) => { // Controls current song and resets time for each song as it changes
        setCurrentTime(0);
        _setCurrentSong(song);
    };

    const play = () => { // Playback control
        setIsPlaying(true);
    };

    const pause = () => { // Playback control
        setIsPlaying(false);
    };

    const togglePlay = () => { // Playback control
        setIsPlaying((prev) => !prev);
    };

    const playFromStart = () => { // Handles initial play action
        if (firstPlay && songs && songs.length > 0) {
            setCurrentSong(songs[0].audio_url);
            setSongTitle(songs[0].title);
            setArtistName(songs[0].artist);
            setAlbumCover(songs[0].album_arts);
            setFirstPlay(false);
            setCurrentlyPlayingSongIndex(0);
            setIsPlaying(true)
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
            songs,
            songTitle,
            updateCurrentView,
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
            setCurrentView,
            currentlyPlayingSongIndex,
            setCurrentlyPlayingSongIndex,
            handleNextTrack,
            handlePreviousTrack,
            currentTrackIndex,
            setCurrentTrackIndex
        }}>
            {children}
        </SongContext.Provider>
    );
};
