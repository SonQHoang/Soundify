import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import { getAllSongs } from "../../store/songs";
import { GetSongsForAlbum } from "../../store/albums";
import DeleteAlbumModal from "../DeleteAlbumModal/DeleteAlbumModal";
import DeleteAlbum from "../DeleteAlbum/DeleteAlbum";
import { AddSongToAlbum, GetSingleAlbum } from "../../store/albums";
// import { getAllAlbums } from "../../store/albums";
import { getUserAlbum } from "../../store/albums";
import Player from "../AudioBar/audiobar";
import "./AlbumDetails.css"
import UpdateAlbum from "../UpdateAlbum/UpdateAlbum";
import UpdateAlbumModal from "../UpdateAlbumModal/UpdateAlbumModal";
import TestSideBar from "../TestComponents/TestSideBar";
import TestNav from "../TestComponents/TestNav";

function AlbumDetails() {
    const { albumId } = useParams()
    const dispatch = useDispatch();
    const history = useHistory()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const new_songs = (useSelector(state => state.album.singleAlbum.songs))
    console.log('new_songs=========> albums component', new_songs)


    const [albumInfo, setAlbumInfo] = useState()
    const [selectedSongs, setSelectedSongs] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [albumToDelete, setAlbumToDelete] = useState(null);
    const [modalType, setModalType] = useState(null);
    const [currentSong, setCurrentSong] = useState(null);

    useEffect(() => {
        // setAlbumInfo(new_songs)
        getAlbumSongs(albumId)
        dispatch(GetSongsForAlbum(albumId))
        dispatch(GetSingleAlbum(albumId))
        dispatch(getAllSongs())
    }, [albumInfo, AddSongToAlbum, dispatch, userId])

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
        // console.log('Selected Song:======>', song)
        if (selectedSongs.includes(song)) {
            setSelectedSongs(selectedSongs.filter((selected) => selected !== song));
        } else {
            setSelectedSongs([...selectedSongs, song])
        }
        setCurrentSong(song)
        setQuery("")
    }

    const addToAlbum = () => {
        Object.values(filteredSongs).map((song) => {
            const song_with_album_id = {
                ...song,
                albumId
            }
            dispatch(AddSongToAlbum(song_with_album_id))
        })
    }

    const getAlbumSongs = async () => {
        await dispatch(GetSongsForAlbum(albumId))
    }

    //======================================================SearchBar End========================================

    //======================================================DeleteAlbum Start========================================


    const currentAlbum = useSelector((state) => state.album.singleAlbum)


    const handleDeleteClick = async () => {
        setAlbumToDelete(currentAlbum)
        // console.log('Album to delete (inside handleDeleteClick):', currentAlbum);
        setModalType("delete");
        setShowModal(true)
        await dispatch(getUserAlbum())
    }

    //======================================================DeleteAlbum End========================================

    //======================================================UpdateAlbum Start========================================

    const [albumToUpdate, setAlbumToUpdate] = useState(null);

    const handleUpdateClick = async () => {
        setAlbumToUpdate(currentAlbum)
        // console.log('Album to delete (inside handleDeleteClick):', currentAlbum);
        setModalType("update");
        setShowModal(true)
        dispatch(getUserAlbum())
    }


    //======================================================UpdateAlbum End========================================

    return (
        <>
            <div className="page-container">
                <TestSideBar />
                <div className="main-content-container">
                    <div className="main-content-nav-container">
                        <TestNav />
                    </div>
                    <div className="main-content">
                        <div className="album-image-and-title-container">
                            <div className="album-image-container">
                                <img className='album-image' src={currentAlbum.album_photo}></img>
                            </div>
                            <div className="album-information-container">
                                <div className="album-album-title-container">
                                    <p>Album</p>
                                    <h1>{currentAlbum?.title}</h1>
                                </div>
                                <div className="album-description">
                                    {currentAlbum?.album_description}
                                </div>
                                <div className="album-user-details">
                                    <img className="album-user-picture" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png"></img>
                                    <p>{currentAlbum?.owner}</p>
                                </div>
                            </div>
                        </div>
                        <div>
                            <button className="album-update-button" onClick={() => {
                                return handleUpdateClick(albumId);
                            }}>Edit Details</button>
                            <UpdateAlbum albumId={albumId} />

                            <button className="album-delete-button" onClick={() => {
                                return handleDeleteClick(albumId);
                            }}>Delete Album</button>
                            <DeleteAlbum albumId={albumId} />
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
                        <div className="album-songs-container">
                            <div className="album-headers">
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
                                <div key={index} className="individual-album-songs">
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        <div>{index + 1}</div>
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
                                        <div className="song-date">{new Date(song.date_created).toLocaleDateString('en-US', {month: 'short', year: 'numeric' })}
                                        </div>
                                    </div>
                                    <div className="grid-row" style={{ width: '200px' }}>
                                        <div className="song-duration">{song.duration}</div>
                                    </div>
                                </div>
                            ))}
                            {selectedSongs.length > 0 && (
                                <div>
                                        <div>
                                            <Player src={currentSong.audio_url} />
                                        </div>
                                </div>
                            )}
                            {showModal && modalType === "update" && (
                                <UpdateAlbumModal
                                    albumId={albumToUpdate.id}
                                    onSubmit={() => {
                                        setShowModal(false);
                                        setAlbumToUpdate(null);
                                        setModalType(null);
                                    }}
                                    onClose={() => {
                                        setShowModal(false);
                                        setAlbumToUpdate(null);
                                        setModalType(null);
                                    }}
                                />
                            )}
                            {showModal && modalType === "delete" && (
                                <DeleteAlbumModal
                                    albumId={albumToDelete.id}
                                    onSubmit={() => {
                                        setShowModal(false);
                                        setAlbumToDelete(null);
                                        setModalType(null);
                                    }}
                                    onClose={() => {
                                        setShowModal(false);
                                        setAlbumToDelete(null);
                                        setModalType(null);
                                    }}
                                />
                            )}
                        </div>
                        <div className="selected-songs">
                            <h3>Album Songs</h3>
                            <ul>
                                {Object.values(filteredSongs).map((song, index) => (
                                    <li key={index}>{song.title}</li>
                                ))}
                            </ul>
                            <button onClick={() => {
                                addToAlbum();
                                getAlbumSongs()
                            }}>Add to Album</button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default AlbumDetails;
