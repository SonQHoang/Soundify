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

function PlaylistDetails() {
    const { playlistId } = useParams()
    console.log('playlistId========>', playlistId)
    const dispatch = useDispatch();
    
    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id
    // const user_tips = useSelector()
    
    //=========================================== Searchbar Start============================================== 
    const [query, setQuery] = useState(""); // Initialize query with an empty string
    const [playlist, setPlaylist] = useState([]); // Initialize playlist as an array of song 
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
    console.log("Are we targeting the playlistToDelete=======>", playlistToDelete)
    const [modalType, setModalType] = useState(null);
    
    const handleDeleteClick = async (playlist) => {
        console.log('Is the handleDeleteClick getting the correct playlist=====>', playlist)
        setPlaylistToDelete(playlist)
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserPlaylist())
    }

    useEffect(() => {
        dispatch(getUserPlaylist())
    }, [dispatch, userId])




    useEffect(() => {
        dispatch(GetSinglePlaylist(playlistId));
    }, [playlistId]);

    //======================================================DeletePlaylist End========================================

    return (
        <>
            <div>
                <button>Edit Details</button>
                <button className="playlist-delete-button" onClick={() => {
                    return handleDeleteClick(playlist)
                }}>Delete Playlist</button>
                <DeletePlaylist playlistId={playlist.id} />
                <input
                    type="text"
                    placeholder="Search for a song"
                    onChange={(e) => setQuery(e.target.value)}
                />
            </div>
            <div className="playlist-details-container">
                {/* <div>#</div>
                <div>Title</div>
                <div>Album</div>
                <div>Date Added</div>
                <div>Time Symbol</div> */}
            </div>
            <div className='search-bar'>
                {filteredSongs.map((value, index) => (
                    <div key={index} onClick={() => addToPlaylist(value.title)}>
                        <p>{value.title}</p>
                    </div>
                ))}
            </div>
            <div className="playlist">
                <h2>Playlist #</h2>
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
        </>
    )
}

export default PlaylistDetails;
