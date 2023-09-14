import React, { useState, useEffect, useContext } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import { getAllSongs } from "../../store/songs";
import { AddSongToPlaylist } from "../../store/playlists";
import DeletePlaylistModal from "../DeletePlaylistModal/DeletePlaylistModal";
import DeletePlaylist from "../DeletePlaylist/DeletePlaylist";
import { GetSinglePlaylist } from "../../store/playlists";
import { getAllPlaylists } from "../../store/playlists";
import { getUserPlaylist } from "../../store/playlists";
import Player from "../AudioBar/audiobar";
import "./PlaylistDetails.css"
import UpdatePlaylist from "../UpdatePlaylist/UpdatePlaylist";
import UpdatePlaylistModal from "../UpdatePlaylistModal/UpdatePlaylistModal";
import { GetSongsForPlaylist } from "../../store/playlists";


function PlaylistDetails() {
    const { playlistId } = useParams()
    console.log('playlistId in playlistDetails========>', playlistId)
    const dispatch = useDispatch();
    const history = useHistory()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    //=========================================== Searchbar Start============================================== 
    const [query, setQuery] = useState(""); // Initialize query with an empty string
    // const [playlist, setPlaylist] = useState([]); // Initialize playlist as an array of song 
    // const [selectedSong, setSelectedSong] = useState(null)

    useEffect(() => {
        console.log('AddSongToPlaylist Thunk fired!')
        dispatch(GetSinglePlaylist(playlistId))
    }, [AddSongToPlaylist])

    const [selectedSongs, setSelectedSongs] = useState([]);

    useEffect(() => {
        dispatch(getAllSongs())
        // dispatch(GetSinglePlaylist(playlistId))
        // console.log('GetAllSongs=========>', getAllSongs())
    }, [dispatch]);

    const songLibrary = Object.values(useSelector(state => state.songs.allSongs));
    const titleKVPairs = songLibrary.map(song => ({
        id: song.id,
        user_id: song.user_id,
        album_id: song.album_id,
        title: song.title,
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

    
    const new_songs = (useSelector(state => state.playlist.singlePlaylist.songs))
    console.log('new_songs=========>', new_songs)
    
    const getPlaylistSongs = async () => {
        await dispatch(GetSongsForPlaylist(playlistId))
        // await dispatch(GetSinglePlaylist(playlistId))
    }

    
    useEffect(() => {
        dispatch(GetSongsForPlaylist(playlistId))
    }, [dispatch])
    //======================================================SearchBar End========================================

    //======================================================DeletePlaylist Start========================================

    const [showModal, setShowModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null);
    // console.log("Are we targeting the playlistToDelete=======>", playlistToDelete)
    const [modalType, setModalType] = useState(null);

    useEffect(() => {
        dispatch(GetSinglePlaylist(playlistId))
        // console.log('Checking that the new playlist is being found==========>', playlistId)
    }, [dispatch, userId])

    const currentPlaylist = useSelector((state) => state.playlist.singlePlaylist)
    // console.log('In Plalyist Details, currentPlaylist======>', currentPlaylist)
    // console.log('In Playlist Details songs?======>', currentPlaylist.songs)


    const handleDeleteClick = async () => {
        setPlaylistToDelete(currentPlaylist)
        // console.log('Playlist to delete (inside handleDeleteClick):', currentPlaylist);
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserPlaylist())
    }

    //======================================================DeletePlaylist End========================================

    //======================================================UpdatePlaylist Start========================================

    const [playlistToUpdate, setPlaylistToUpdate] = useState(null);

    useEffect(() => {
        dispatch(GetSinglePlaylist(playlistId))
    }, [dispatch, userId])

    const handleUpdateClick = async () => {
        setPlaylistToUpdate(currentPlaylist)
        // console.log('Playlist to delete (inside handleDeleteClick):', currentPlaylist);
        setModalType("update");
        setShowModal(true)
        dispatch(getUserPlaylist())
    }


    //======================================================UpdatePlaylist End========================================


    return (
        <>
            <div className="playlist-details-container">
                <div className="playlist-info-container">
                    <div className="playlist-image-and-title-container">
                        <div className="playlist-image">
                            <h2>Playlist Graphic Here</h2>
                        </div>
                        <div className="playlist-information-container">
                            <p>Playlist</p>
                            <h2>{currentPlaylist?.title} {currentPlaylist?.id}</h2>
                            <div className="playlist-description">
                                {currentPlaylist?.playlist_description}
                            </div>
                            <div className="playlist-user-details">
                                <p className="playlist-user-picture">Profile Pic</p>
                                <p>{currentPlaylist?.owner}</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button className="playlist-update-button" onClick={() => {
                            return handleUpdateClick(playlistId);
                        }}>Edit Details</button>
                        <UpdatePlaylist playlistId={playlistId} />

                        <button className="playlist-delete-button" onClick={() => {
                            return handleDeleteClick(playlistId);
                        }}>Delete Playlist</button>
                        <DeletePlaylist playlistId={playlistId} />
                    </div>
                </div>
                <div className='search-bar-container'>
                    <div className='search-bar'>
                        <input
                            type="text"
                            placeholder="Search for a song"
                            onChange={(e) => setQuery(e.target.value)}
                        />
                    </div>
                </div>
                <div className="playlist-headers">
                    <p>#</p>
                    <p>Title</p>
                    <p>Album</p>
                    <p>Date Added</p>
                    <p></p>
                    <p>Clock Icon</p>
                </div>
                <div className="playlist-songs-container">
                    <div className="playlist">
                        {/* <div>
                            {(new_songs)?.map((song, index) => (
                                <div>
                                    <p>{song.title}</p>
                                    <p>{song.id}</p>
                                </div>
                            ))}
                        </div> */}
                            {(new_songs)?.map((song, index) => (
                                <div key={index} className="individual-playlist-songs">
                                    {song?.title ? (
                                        <p onClick={() => { selectSong(song); setQuery("") }}>{song.title}</p>
                                    ) : null}
                                    <p>{song.date_created}</p>
                                </div>
                            ))}
                        {selectedSongs.length > 0 && (
                            <div>
                                {selectedSongs.map((selectedSong, index) => (
                                    <div key={index}>
                                        <Player src={selectedSong.audio_url} /> {/* Play each selected song */}
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                    {/* {selectedSongs.map((song, index) => (
                        <Player key={index} src={song.audio_url} />
                    ))} */}
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
                    <div className="selected-songs">
                        <h3>Playlist Songs</h3>
                        <ul>
                            {Object.values(filteredSongs).map((song, index) => (
                                <li key={index}>{song.title}</li>
                            ))}
                        </ul>
                        <button onClick={() => {
                            addToPlaylist();
                            // getPlaylistSongs();
                        }}>Queue Songs</button>
                        <button onClick={() => {
                            getPlaylistSongs()
                        }}>Add to Playlist
                        </button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default PlaylistDetails;
