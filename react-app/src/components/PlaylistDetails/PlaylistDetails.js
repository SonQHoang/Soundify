import React, { useState, useEffect, useContext } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import { getAllSongs } from "../../store/songs";
import { AddSongToPlaylist } from "../../store/playlists";
import DeletePlaylistModal from "../DeletePlaylistModal/DeletePlaylistModal";
import DeletePlaylist from "../DeletePlaylist/DeletePlaylist";
import { GetSinglePlaylist } from "../../store/playlists";
import { getUserPlaylist } from "../../store/playlists";
import Player from "../AudioBar/audiobar";
import UpdatePlaylist from "../UpdatePlaylist/UpdatePlaylist";
import UpdatePlaylistModal from "../UpdatePlaylistModal/UpdatePlaylistModal";
import { GetSongsForPlaylist } from "../../store/playlists";
import TestSideBar from "../TestComponents/TestSideBar";
import TestNav from "../TestComponents/TestNav";
import { SongContext } from "../../context/SongContext";
import Footer from "../Footer/Footer";
import "./PlaylistDetails.css"

function PlaylistDetails() {
    const { playlistId } = useParams()
    const dispatch = useDispatch();

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const new_songs = (useSelector(state => state.playlist.singlePlaylist.songs))

    const [playlistInfo, setPlaylistInfo] = useState(new_songs)
    const [selectedSongs, setSelectedSongs] = useState([])
    const [showModal, setShowModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null);
    const [modalType, setModalType] = useState(null);
    const { play, currentSong, setCurrentSong } = useContext(SongContext);
    const [isDropdownOpen, setIsDropdownOpen] = useState(false)

    const toggleDropdown = () => setIsDropdownOpen(!isDropdownOpen);

    useEffect(() => {
        getPlaylistSongs(playlistId)
        dispatch(GetSongsForPlaylist(playlistId))
        dispatch(GetSinglePlaylist(playlistId))
        dispatch(getAllSongs())
    }, [playlistInfo, AddSongToPlaylist, dispatch, userId])

    //=========================================== Searchbar Start============================================== 
    const [query, setQuery] = useState(""); // Initialize query with an empty string


    const songLibrary = Object.values(useSelector(state => state.songs.allSongs));
    const titleKVPairs = songLibrary.map(song => ({
        id: song.id,
        user_id: song.user_id,
        album_id: song.album_id,
        title: song.title,
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

    const selectSong = (song) => {
        if (selectedSongs.includes(song)) {
            setSelectedSongs(selectedSongs.filter((selected) => selected !== song));
        } else {
            setSelectedSongs([...selectedSongs, song])
        }
        setCurrentSong(song.audio_url)
        play()
        setQuery("")
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

    const getPlaylistSongs = async () => {
        await dispatch(GetSongsForPlaylist(playlistId))
    }

    //======================================================SearchBar End========================================

    //======================================================DeletePlaylist Start========================================

    const currentPlaylist = useSelector((state) => state.playlist.singlePlaylist)
    const isOwner = currentPlaylist.owner === sessionUser.first_name


    const handleDeleteClick = async () => {
        setPlaylistToDelete(currentPlaylist)
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserPlaylist())
    }

    //======================================================DeletePlaylist End========================================

    //======================================================UpdatePlaylist Start========================================

    const [playlistToUpdate, setPlaylistToUpdate] = useState(null);

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
                        <div className='search-bar-container'>
                            <div className="play-button-playlist-container">
                                <button className='play-playlist-button'>
                                    <img className="play-button-playlist" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695962350/Untitled_design_4_olkf9a.png" alt="play button" />
                                </button>
                            </div>
                            <div className='search-bar'>
                                <input
                                    type="text"
                                    placeholder="Search for a song"
                                    onChange={(e) => setQuery(e.target.value)}
                                />
                            </div>
                        </div>
                        <div className="playlist-songs-container">
                            <div className="playlist-headers">
                                <div className="grid-row" style={{ width: '200px' }}>
                                    <div>#</div>
                                </div>
                                <div className="grid-row" style={{ width: '200px' }}>
                                    <div>Title</div>
                                </div>
                                <div className="grid-row" style={{ width: '200px' }}>
                                    <div>Album</div>
                                </div>
                                <div className="grid-row" style={{ width: '200px' }}>
                                    <div>Date Added</div>
                                </div>
                                <div className="grid-row" style={{ width: '200px' }}>
                                    <img className='clock-icon' src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695032037/icons8-clock-32_bel47j.png" alt="clock-icon"></img>
                                </div>
                            </div>
                            {(new_songs)?.map((song, index) => (
                                <div key={index} className="individual-playlist-songs">
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        <div className="playlist-song-count">{index + 1}</div>
                                    </div>
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        {song?.title ? (
                                            <p onClick={() => { selectSong(song); setQuery("") }}>{song.title}</p>
                                        ) : null}
                                    </div>
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        <div className="album-info">Album Info</div>
                                    </div>
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        <div className="song-date">{new Date(song.date_created).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })}
                                        </div>
                                    </div>
                                    <div className="grid-row" id="time-info" style={{ width: '200px' }}>
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
                        <div className="selected-songs">
                            <h3>Playlist Songs</h3>
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
            {/* <div>
                <Player src={currentSong ? currentSong.audio_url : null} />
            </div> */}
        </>
    )
}

export default PlaylistDetails;
