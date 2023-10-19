import React, { useState, useEffect, useContext } from "react";
import { AddSongToPlaylist, GetSinglePlaylist, getUserPlaylist, GetSongsForPlaylist } from "../../store/playlists";
import { getAllSongs } from "../../store/songs";
import { SongContext } from "../../context/SongContext";
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom"
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
import DeletePlaylistModal from "../DeletePlaylistModal/DeletePlaylistModal";
import UpdatePlaylistModal from "../UpdatePlaylistModal/UpdatePlaylistModal";
import TestSideBar from "../TestComponents/TestSideBar";
import TestNav from "../TestComponents/TestNav";
import "./PlaylistDetails.css"

function PlaylistDetails() {

    // Retrieving data from Redux store
    const sessionUser = useSelector(state => state.session.user);
    const new_songs = useSelector(state => state.playlist.singlePlaylist.songs);
    const songLibrary = Object.values(useSelector(state => state.songs.allSongs));
    const currentPlaylist = useSelector((state) => state.playlist.singlePlaylist);

    // URL params
    const { playlistId } = useParams();

    // Local component state
    const [isLoading, setIsLoading] = useState(true);
    const [query, setQuery] = useState("");
    const [selectedSongs, setSelectedSongs] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null);
    const [playlistToUpdate, setPlaylistToUpdate] = useState(null);
    const [modalType, setModalType] = useState(null);
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const [hoveredSongIndex, setHoveredSongIndex] = useState(null);
    const [currentlyPlayingSongIndex, setCurrentlyPlayingSongIndex] = useState(null);
    // const [currentSongUrl, setCurrentSongUrl] = useState('');
    const [playingPlaylistId, setPlayingPlaylistId] = useState(null);
    const toggleDropdown = () => setIsDropdownOpen(!isDropdownOpen);
    const [isPlaylistPlayed, setIsPlaylistPlayed] = useState(false);

    // Context
    const { play, isPlaying, setCurrentSong, setSongTitle, setArtistName, setAlbumCover, playFromStart, setFirstPlay, updateCurrentView } = useContext(SongContext);

    // Dispatch
    const dispatch = useDispatch();

    const getPlaylistSongs = async () => {
        await dispatch(GetSongsForPlaylist(playlistId))
    }

    // const playFromStartModified = () => {
    //     if (!isPlaylistPlayed || playingPlaylistId !== playlistId) {
    //         setIsPlaylistPlayed(true);
    //     }
    //     playFromStart();
    // };

    useEffect(() => {
        const fetchData = async () => {
            await Promise.all([
                dispatch(GetSongsForPlaylist(playlistId)),
                dispatch(GetSinglePlaylist(playlistId)),
                dispatch(getAllSongs())
            ])

            setIsLoading(false)
            setFirstPlay(true)
            setIsPlaylistPlayed(false)
        }
        fetchData()
    }, [dispatch, playlistId])


    useEffect(() => {
        updateCurrentView('playlist');
        return () => {
            updateCurrentView('album');
        }
    }, []);

    if (isLoading) {
        return <LoadingSpinner />
    }



    //=========================================== Searchbar Start============================================== 
    const titleKVPairs = songLibrary.map(song => ({
        id: song.id,
        user_id: song.user_id,
        album_id: song.album_id,
        title: song.title,
        artist: song.artist,
        duration: song.duration,
        audio_url: song.audio_url,
        lyrics: song.lyrics,
        date_created: song.date_created
    }));

    const queryFilter = (query, titleKVPairs) => {
        if (!query) {
            return []
        }
        return titleKVPairs.filter(song => song.title.includes(query))
    }

    const filteredSongs = queryFilter(query, titleKVPairs);

    const selectSong = (song, index) => {
        if (selectedSongs.includes(song)) {
            setSelectedSongs(selectedSongs.filter((selected) => selected !== song));
        } else {
            setSelectedSongs([...selectedSongs, song])
        }
        setCurrentSong(song.audio_url);
        setSongTitle(song.title);
        setArtistName(song.artist);
        setAlbumCover(song.album_arts);
        setCurrentlyPlayingSongIndex(index);
        setQuery("")
        play()
    }


    const addToPlaylist = () => {
        Object.values(filteredSongs).map((song) => {
            const song_with_playlist_id = {
                ...song,
                playlistId
            }
            dispatch(AddSongToPlaylist(song_with_playlist_id))
        })
    }


    //======================================================SearchBar End========================================

    //======================================================DeletePlaylist Start========================================

    const isOwner = currentPlaylist.owner === sessionUser.first_name

    const handleDeleteClick = async () => {
        setPlaylistToDelete(currentPlaylist)
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserPlaylist())
    }

    //======================================================DeletePlaylist End========================================

    //======================================================UpdatePlaylist Start========================================

    const handleUpdateClick = async () => {
        setPlaylistToUpdate(currentPlaylist)
        setModalType("update");
        setShowModal(true)
        dispatch(getUserPlaylist())
    }

    //======================================================UpdatePlaylist End========================================

    return (
        <>
            <div className="page-container">
                <TestSideBar />
                <div className="main-content-container">
                    <div className="main-content-nav-container">
                        <TestNav />
                    </div>
                    <div className="main-content">
                        <div className="playlist-image-and-title-container">
                            <div className="playlist-image-container">
                                <img className='playlist-image' src={currentPlaylist.image}></img>
                            </div>
                            <div className="playlist-information-container">
                                <div className="playlist-playlist-title-container">
                                    <p>Playlist</p>
                                    <h1>{currentPlaylist?.title}</h1>
                                </div>
                                <div className="playlist-description">
                                    {currentPlaylist?.playlist_description}
                                </div>
                                <div className="playlist-user-details">
                                    <img className="playlist-user-picture" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png"></img>
                                    <p>{currentPlaylist?.owner}</p>
                                </div>
                            </div>
                        </div>
                        <div className='search-bar-container'>
                            <div className="play-button-playlist-container">
                                {/* <button className='play-playlist-button' onClick={playFromStartModified}> */}
                                    <img
                                        className={
                                            isPlaying && playingPlaylistId === playlistId ? "pause-button" : "play-button"
                                        } src={isPlaying && playingPlaylistId === playlistId
                                            ? "https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697655841/icons8-pause-64_uryer0.png"
                                            : "https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697656383/icons8-play-50_fok8tu.png"}
                                        alt="play button"
                                    />
                                {/* </button> */}
                            </div>
                            {isOwner && (
                                <div className="playlist-options-dropdown">
                                    <button className="playlist-dropdown-button" onClick={toggleDropdown}>. . .</button>
                                    {isDropdownOpen && (
                                        <div className="dropdown-content">
                                            <button className="playlist-update-button" onClick={() => {
                                                setIsDropdownOpen(false);
                                                return handleUpdateClick(playlistId);
                                            }}>Edit Details</button>

                                            <button className="playlist-delete-button" onClick={() => {
                                                setIsDropdownOpen(false);
                                                return handleDeleteClick(playlistId);
                                            }}>Delete Playlist</button>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                        <div className="playlist-songs-container">
                            <div className="playlist-headers">
                                <div className=" hashtag-header">
                                    <div>#</div>
                                </div>
                                <div className=" title-header">
                                    <div>Title</div>
                                </div>
                                <div className=" album-header">
                                    <div>Album</div>
                                </div>
                                <div className=" date-header">
                                    <div>Date Added</div>
                                </div>
                                <div className=" time-header">
                                    <img className='clock-icon' src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695032037/icons8-clock-32_bel47j.png" alt="clock-icon"></img>
                                </div>
                            </div>
                            {(new_songs)?.map((song, index) => (
                                <div key={index}
                                    className="individual-playlist-songs"
                                    onMouseEnter={() => setHoveredSongIndex(index)}
                                    onMouseLeave={() => setHoveredSongIndex(null)}
                                    onClick={() => {
                                        selectSong(song, index);
                                    }}
                                >
                                    <div className="grid-row">
                                        <div className="playlist-song-count">
                                            {isPlaying && currentlyPlayingSongIndex === index
                                                ? <img className="song-audio-gif" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697659865/Nt6v_qjkqxz.gif" alt="Playing" />
                                                : (hoveredSongIndex === index
                                                    ? <img className="song-play-icon-playlist" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697657626/icons8-play-48_1_ieduyg.png" alt="Play" />
                                                    : index + 1)}
                                        </div>
                                    </div>
                                    <div className="grid-row">
                                        {song?.title ? (
                                            <div className="song-item" onClick={(e) => { e.stopPropagation(); selectSong(song, index); setQuery("") }}>
                                                <div className="song-image-container">
                                                    <img src={song.album_arts[0]} alt="Album Art" />
                                                </div>
                                                <p>{song.title}</p>
                                            </div>
                                        ) : null}
                                    </div>
                                    <div className="grid-row album-title">
                                        {song?.album_titles?.map((albumTitle, index) => (
                                            <p key={index}>{albumTitle}</p>
                                        ))}
                                    </div>
                                    <div className="grid-row">
                                        <div className="song-date">{new Date(song.date_created).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })}</div>
                                    </div>
                                    <div className="grid-row" id="time-info">
                                        <div className="song-duration">{song.duration}</div>
                                    </div>
                                </div>
                            ))}
                            {showModal && modalType === "update" && (
                                <UpdatePlaylistModal
                                    playlistId={playlistToUpdate.id}
                                    onSubmit={() => {
                                        setShowModal(false);
                                        setPlaylistToUpdate(null);
                                        setModalType(null);
                                    }}
                                    onClose={() => {
                                        setShowModal(false);
                                        setPlaylistToUpdate(null);
                                        setModalType(null);
                                    }}
                                />
                            )}
                            {showModal && modalType === "delete" && (
                                <DeletePlaylistModal
                                    playlistId={playlistToDelete.id}
                                    onSubmit={() => {
                                        setShowModal(false);
                                        setPlaylistToDelete(null);
                                        setModalType(null);
                                    }}
                                    onClose={() => {
                                        setShowModal(false);
                                        setPlaylistToDelete(null);
                                        setModalType(null);
                                    }}
                                />
                            )}
                        </div>
                        <h3>Playlist Songs</h3>
                        <div className="selected-songs">
                            <div className='search-bar'>
                                <input
                                    type="text"
                                    placeholder="Search for a song"
                                    onChange={(e) => setQuery(e.target.value)}
                                />
                            </div>
                            <ul>
                                {Object.values(filteredSongs).map((song, index) => (
                                    <li key={index}>{song.title}</li>
                                ))}
                            </ul>
                            <button onClick={() => {
                                addToPlaylist();
                                getPlaylistSongs()
                            }}>Add to Playlist</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default PlaylistDetails;
