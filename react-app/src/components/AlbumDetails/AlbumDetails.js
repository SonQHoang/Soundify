import React, { useState, useEffect } from "react";
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
import "./AlbumDetails.css"
import UpdatePlaylist from "../UpdatePlaylist/UpdatePlaylist";
import UpdatePlaylistModal from "../UpdatePlaylistModal/UpdatePlaylistModal";

function AlbumDetails() {
    const { albumId } = useParams()
    // console.log('playlistId in playlistDetails========>', playlistId)
    const dispatch = useDispatch();
    const history = useHistory()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id
    // const user_tips = useSelector()

    //=========================================== Searchbar Start============================================== 
    const [query, setQuery] = useState(""); // Initialize query with an empty string
    // const [playlist, setPlaylist] = useState([]); // Initialize playlist as an array of song 
    // const [selectedSong, setSelectedSong] = useState(null)
    const [selectedSongs, setSelectedSongs] = useState([]);

    const new_songs = useSelector((state) => state.playlist.singlePlaylist);
    console.log('Updated Song List=========>', new_songs)

    useEffect(() => {
        dispatch(getAllSongs())
    }, [dispatch]);

    const songLibrary = Object.values(useSelector(state => state.songs.allSongs));
    const titleKVPairs = songLibrary.map(song => ({ title: song.title, audio_url: song.audio_url }));

    const queryFilter = (query, titleKVPairs) => {
        if (!query) {
            return []
        }
        return titleKVPairs.filter(song => song.title.includes(query))
    }

    const filteredSongs = queryFilter(query, titleKVPairs);

    const addToPlaylist = async (title) => {
        const selectedSong = songLibrary.find(song => song.title === title);
        if (selectedSong) {
            setSelectedSongs([...selectedSongs, selectedSong]);
            dispatch(AddSongToPlaylist(selectedSong));
            setQuery("");
        }
    }

    const selectSong = (song) => {
        console.log('Selected Song:======>', song)
        if (selectedSongs.includes(song)) {
            setSelectedSongs(selectedSongs.filter((selected) => selected !== song));
        } else {
            setSelectedSongs([...selectedSongs, song])
        }
        dispatch(AddSongToPlaylist(song))
        setQuery("")
    }

    //======================================================SearchBar End========================================

    //======================================================DeletePlaylist Start========================================

    const [showModal, setShowModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null);
    // console.log("Are we targeting the playlistToDelete=======>", playlistToDelete)
    const [modalType, setModalType] = useState(null);

    useEffect(() => {
        dispatch(GetSinglePlaylist(albumId))
    }, [dispatch, userId])

    const currentPlaylist = useSelector((state) => state.playlist.singlePlaylist)
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
        dispatch(GetSinglePlaylist(albumId))
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
            <div className="album-details-container">
                <div className="album-info-container">
                    <div className="album-image-and-title-container">
                        <div className="album-image">
                            <h2>Album Graphic Here</h2>
                        </div>
                        <div className="album-information-container">
                            <p>Album</p>
                            <h2>{currentPlaylist?.title} {currentPlaylist?.id}</h2>
                            <div className="album-description">
                                {currentPlaylist?.playlist_description}
                            </div>
                            <div className="album-user-details">
                                <p className="album-user-picture">Profile Pic</p>
                                <p>{currentPlaylist?.owner}</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button className="album-update-button" onClick={() => {
                            return handleUpdateClick(albumId);
                        }}>Edit Details</button>
                        <UpdatePlaylist albumId={albumId} />

                        <button className="playlist-delete-button" onClick={() => {
                            return handleDeleteClick(albumId);
                        }}>Delete Album</button>
                        <DeletePlaylist albumId={albumId} />
                    </div>
                </div>
                <div className='search-bar-container'>
                    <div className='search-bar'>
                        {filteredSongs.map((value, index) => (
                            <div key={index} onClick={() => addToPlaylist(value.title)}>
                                <p>{value.title}</p>
                            </div>
                        ))}
                        <input
                            type="text"
                            placeholder="Search for a song"
                            onChange={(e) => setQuery(e.target.value)}
                        />
                    </div>
                </div>
                <div className="album-headers">
                    <p>#</p>
                    <p>Title</p>
                    <p>Reaction</p>
                    <p>Clock Icon</p>
                </div>
                <div className="album-songs-container">
                    <div className="album">
                        <ul>
                            {Object.values(new_songs)?.map((song, index) => (
                                <div key={index}>
                                    {song?.title ? (
                                        <p onClick={() => { selectSong(song); setQuery("") }}>{song.title}</p>
                                    ) : null}
                                    <p>{song?.album}</p>
                                    <p>{song?.dateAdded}</p>
                                    <p>{song?.timeSymbol}</p>
                                </div>
                            ))}
                        </ul>
                    </div>
                    {selectedSongs.map((song, index) => (
                        <Player key={index} src={song.audio_url} />
                    ))}
                    {showModal && modalType === "update" && (
                        <UpdatePlaylistModal
                            albumId={playlistToUpdate.id}
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
                            albumId={playlistToDelete.id}
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
            </div >
        </>
    )
}

export default AlbumDetails;
