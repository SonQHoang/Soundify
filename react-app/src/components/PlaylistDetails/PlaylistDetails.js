import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
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

function PlaylistDetails() {
    const { playlistId } = useParams()
    // console.log('playlistId in playlistDetails========>', playlistId)
    const dispatch = useDispatch();

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id
    // const user_tips = useSelector()

    //=========================================== Searchbar Start============================================== 
    const [query, setQuery] = useState(""); // Initialize query with an empty string
    // const [playlist, setPlaylist] = useState([]); // Initialize playlist as an array of song 
    const [selectedSong, setSelectedSong] = useState(null)

    const singlePlaylist = useSelector((state) => state.playlist);
    const playlist_song = Object.values(singlePlaylist)
    const playlist_music = playlist_song[1]

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
            dispatch(AddSongToPlaylist(selectedSong))
        }
    }

    const selectSong = (song) => {
        console.log('Selected Song:======>', song)
        setSelectedSong(song);
    }

    //======================================================SearchBar End========================================

    //======================================================DeletePlaylist Start========================================

    const [showModal, setShowModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null);
    // console.log("Are we targeting the playlistToDelete=======>", playlistToDelete)
    const [modalType, setModalType] = useState(null);

    useEffect(() => {
        dispatch(GetSinglePlaylist(playlistId))
    }, [dispatch, userId])

    const currentPlaylist = useSelector((state) => state.playlist.singlePlaylist)
    // console.log('currentPlaylist======>', currentPlaylist)

    const handleDeleteClick = async () => {
        setPlaylistToDelete(currentPlaylist)
        // console.log('Playlist to delete (inside handleDeleteClick):', currentPlaylist);
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserPlaylist())
    }


    // useEffect(() => {
    //     dispatch(GetSinglePlaylist(playlistId));
    // }, [playlistId]);

    //======================================================DeletePlaylist End========================================

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
                            <h2>User Inputted Title Should Go Here #(PlaylistNumber)</h2>
                            <div className="playlist-description">
                                PlaylistDescription goes here
                            </div>
                            <div className="playlist-user-details">
                                <p>User Profile Pic Here</p>
                                <p>User's Name goes here</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button>Edit Details</button>
                        <button className="playlist-delete-button" onClick={() => {
                            // console.log('Playlist ID=======>:', playlistId);
                            return handleDeleteClick(playlistId);
                        }}>Delete Playlist</button>
                        <DeletePlaylist playlistId={playlistId} />
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
                        <ul>
                            {Object.values(playlist_music).map((song, index) => (
                                <div key={index}>
                                    {song?.title ? (
                                        <p onClick={() => { song?.title && selectSong(song); setQuery("") }}>{song?.title}</p>
                                    ) : null}
                                    <p>{song?.album}</p>
                                    <p>{song?.dateAdded}</p>
                                    <p>{song?.timeSymbol}</p>
                                </div>
                            ))}
                        </ul>
                    </div>
                    {selectedSong && <Player src={selectedSong.audio_url} />}

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
            </div >
        </>
    )
}

export default PlaylistDetails;
