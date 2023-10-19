// import React, { useState, useEffect, useContext } from "react";
// import { AddSongToAlbum, GetSingleAlbum, getUserAlbum } from "../../store/albums";
// import { getAllSongs } from "../../store/songs";
// import { GetSongsForAlbum } from "../../store/albums";
// import { SongContext } from "../../context/SongContext";
// import { useSelector, useDispatch } from 'react-redux';
// import { useParams } from "react-router-dom";
// import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
// import DeleteAlbumModal from "../DeleteAlbumModal/DeleteAlbumModal";
// import UpdateAlbumModal from "../UpdateAlbumModal/UpdateAlbumModal";
// import TestSideBar from "../TestComponents/TestSideBar";
// import TestNav from "../TestComponents/TestNav";
// import "./AlbumDetails.css"

// function AlbumDetails() {
//     const dispatch = useDispatch();
    
//     const sessionUser = useSelector(state => state.session.user)
//     const userId = sessionUser.id
//     const new_songs = (useSelector(state => state.album.singleAlbum.songs))
//     const songLibrary = Object.values(useSelector(state => state.songs.allSongs));
//     const currentAlbum = useSelector((state) => state.album.singleAlbum)
    
//     const { albumId } = useParams()
    
//     const [isLoading, setIsLoading] = useState(true);
//     const [query, setQuery] = useState("");
//     const [selectedSongs, setSelectedSongs] = useState([]);
//     const [showModal, setShowModal] = useState(false);
//     const [albumToDelete, setAlbumToDelete] = useState(null);
//     const [albumToUpdate, setAlbumToUpdate] = useState(null);
//     const [modalType, setModalType] = useState(null);
//     const [isDropdownOpen, setIsDropdownOpen] = useState(false)
//     const [hoveredSongIndex, setHoveredSongIndex] = useState(null);
//     const [currentlyPlayingSongIndex, setCurrentlyPlayingSongIndex] = useState(null);
//     const [playingAlbumId, setPlayingAlbumId] = useState(null);
//     const toggleDropdown = () => setIsDropdownOpen(!isDropdownOpen);
//     const [isAlbumPlayed, setIsAlbumPlayed] = useState(false);
//     const [albumInfo, setAlbumInfo] = useState()

//     const { play, pause, togglePlay, isPlaying, setCurrentSong, setSongTitle, setArtistName, setAlbumCover, firstPlay, playFromStart, setFirstPlay, updateCurrentView } = useContext(SongContext);

//     const playFromStartModified = () => {
//         if (!isAlbumPlayed || playingAlbumId !== albumId) {
//             setIsAlbumPlayed(true);
//             setPlayingAlbumId(albumId);
//         }
//         playFromStart();
//     };
//     useEffect(() => {
//         const fetchData = async () => {
//             await Promise.all([
//                 dispatch(GetSongsForAlbum(albumId)),
//                 dispatch(GetSingleAlbum(albumId)),
//                 dispatch(getAllSongs())
//             ]);

//             setIsLoading(false);
//             setFirstPlay(true);
//             setIsAlbumPlayed(false);
//         };

//         fetchData();
//     }, [dispatch, albumId]);


//     useEffect(() => {
//         updateCurrentView('album');
//         return () => {
//             updateCurrentView('playlist');
//         }
//     }, []);


//     if (isLoading) {
//         return <LoadingSpinner />
//     }

//     //=========================================== Searchbar Start============================================== 

//     const titleKVPairs = songLibrary.map(song => ({
//         id: song.id,
//         user_id: song.user_id,
//         album_id: song.album_id,
//         title: song.title,
//         duration: song.duration,
//         audio_url: song.audio_url,
//         lyrics: song.lyrics,
//         date_created: song.date_created
//     }));

//     const queryFilter = (query, titleKVPairs) => {
//         if (!query) {
//             return []
//         }
//         return titleKVPairs.filter(song => song.title.includes(query))
//     }

//     const filteredSongs = queryFilter(query, titleKVPairs);

//     const selectSong = (song, index) => {
//         if (selectedSongs.includes(song)) {
//             setSelectedSongs(selectedSongs.filter((selected) => selected !== song));
//         } else {
//             setSelectedSongs([...selectedSongs, song])
//         }
//         setCurrentSong(song.audio_url);
//         setSongTitle(song.title);
//         setArtistName(song.artist);
//         setAlbumCover(song.album_arts);
//         setCurrentlyPlayingSongIndex(index);
//         setQuery("")
//         play()
//     }

//     const addToAlbum = () => {
//         Object.values(filteredSongs).map((song) => {
//             const song_with_album_id = {
//                 ...song,
//                 albumId
//             }
//             dispatch(AddSongToAlbum(song_with_album_id))
//         })
//     }
//     //======================================================SearchBar End========================================

//     //======================================================DeleteAlbum Start========================================


//     const isOwner = currentAlbum.owner === sessionUser.first_name

//     const handleDeleteClick = async () => {
//         setAlbumToDelete(currentAlbum)
//         setModalType("delete");
//         setShowModal(true)
//         await dispatch(getUserAlbum())
//     }

//     //======================================================DeleteAlbum End========================================

//     //======================================================UpdateAlbum Start========================================

//     const handleUpdateClick = async () => {
//         setAlbumToUpdate(currentAlbum)
//         setModalType("update");
//         setShowModal(true)
//         dispatch(getUserAlbum())
//     }


//     //======================================================UpdateAlbum End========================================

//     return (
//         <>
//             <div className="page-container">
//                 <TestSideBar />
//                 <div className="main-content-container">
//                     <div className="main-content-nav-container">
//                         <TestNav />
//                     </div>
//                     <div className="main-content">
//                         <div className="album-image-and-title-container">
//                             <div className="album-image-container">
//                                 <img className='album-image' src={currentAlbum.album_photo} alt="album-cover"></img>
//                             </div>
//                             <div className="album-information-container">
//                                 <div className="album-album-title-container">
//                                     <p>Album</p>
//                                     <h1>{currentAlbum?.title}</h1>
//                                 </div>
//                                 <div className="album-description">
//                                     {currentAlbum?.album_description}
//                                 </div>
//                                 <div className="album-user-details">
//                                     <img className="album-user-picture" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png" alt="current-user"></img>
//                                     <p>{currentAlbum?.owner}</p>
//                                 </div>
//                             </div>
//                         </div>
//                         <div className="play-button-albums-container">
//                             <button className='play-albums-button' onClick={playFromStartModified}>
//                                 <img
//                                      className={
//                                         isPlaying && playingAlbumId === albumId ? "pause-button" : "play-button"
//                                     } src={isPlaying && playingAlbumId === albumId
//                                         ? "https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697655841/icons8-pause-64_uryer0.png"
//                                         : "https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697656383/icons8-play-50_fok8tu.png"}
//                                     alt="play button"
//                                 />
//                             </button>
//                         </div>
//                         {isOwner && (
//                             <div className="album-options-dropdown">
//                                 <button className="album-dropdown-button" onClick={toggleDropdown}>. . .</button>
//                                 {isDropdownOpen && (
//                                     <div className="dropdown-content">
//                                         <button className="album-update-button" onClick={() => {
//                                             setIsDropdownOpen(false);
//                                             return handleUpdateClick(albumId);
//                                         }}>Edit Details</button>

//                                         <button className="album-delete-button" onClick={() => {
//                                             setIsDropdownOpen(false);
//                                             return handleDeleteClick(albumId);
//                                         }}>Delete Album</button>
//                                     </div>
//                                 )}
//                             </div>
//                         )}
//                         <div className="album-songs-container">
//                             <div className="album-headers">
//                                 <div className="grid-row grid-row-width">
//                                     <div>#</div>
//                                 </div>
//                                 <div className="grid-row grid-row-width">
//                                     <div>Title</div>
//                                 </div>
//                                 <div className="grid-row grid-row-width">
//                                     <div>Date Added</div>
//                                 </div>
//                                 <div className="grid-row grid-row-width">
//                                     <img className='clock-icon' src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695032037/icons8-clock-32_bel47j.png" alt="clock-icon"></img>
//                                 </div>
//                             </div>
//                             {(new_songs)?.map((song, index) => (
//                                 <div key={index}
//                                     className="individual-album-songs"
//                                     onMouseEnter={() => setHoveredSongIndex(index)}
//                                     onMouseLeave={() => setHoveredSongIndex(null)}
//                                     onClick={() => {
//                                         selectSong(song, index);
//                                     }}
//                                 >
//                                     <div className="grid-row grid-row-width">
//                                         {isPlaying && currentlyPlayingSongIndex === index
//                                             ? <img className="song-audio-gif" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697659865/Nt6v_qjkqxz.gif" alt="Playing" />
//                                             : (hoveredSongIndex === index
//                                                 ? <img className="song-play-icon-playlist" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1697657626/icons8-play-48_1_ieduyg.png" alt="Play" />
//                                                 : index + 1)}
//                                     </div>
//                                     <div className="grid-row grid-row-width">
//                                         {song?.title ? (
//                                             <p onClick={(e) => { e.stopPropagation(); selectSong(song, index); setQuery("") }}>{song.title}</p>
//                                         ) : null}
//                                     </div>
//                                     <div className="grid-row grid-row-width">
//                                         <div className="song-date">{new Date(song.date_created).toLocaleDateString('en-US', { month: 'short', year: 'numeric' })}
//                                         </div>
//                                     </div>
//                                     <div className="grid-row grid-row-width">
//                                         <div className="song-duration">{song.duration}</div>
//                                     </div>
//                                 </div>
//                             ))}
//                             {showModal && modalType === "update" && (
//                                 <UpdateAlbumModal
//                                     albumId={albumToUpdate.id}
//                                     onSubmit={() => {
//                                         setShowModal(false);
//                                         setAlbumToUpdate(null);
//                                         setModalType(null);
//                                     }}
//                                     onClose={() => {
//                                         setShowModal(false);
//                                         setAlbumToUpdate(null);
//                                         setModalType(null);
//                                     }}
//                                 />
//                             )}
//                             {showModal && modalType === "delete" && (
//                                 <DeleteAlbumModal
//                                     albumId={albumToDelete.id}
//                                     onSubmit={() => {
//                                         setShowModal(false);
//                                         setAlbumToDelete(null);
//                                         setModalType(null);
//                                     }}
//                                     onClose={() => {
//                                         setShowModal(false);
//                                         setAlbumToDelete(null);
//                                         setModalType(null);
//                                     }}
//                                 />
//                             )}
//                         </div>
//                         <div className="selected-songs">
//                             <h3>Album Songs</h3>
//                             <div className='search-bar'>
//                             <input
//                                 type="text"
//                                 placeholder="Search for a song"
//                                 onChange={(e) => setQuery(e.target.value)}
//                             />
//                         </div>
//                             <ul>
//                                 {Object.values(filteredSongs).map((song, index) => (
//                                     <li key={index}>{song.title}</li>
//                                 ))}
//                             </ul>
//                             <button onClick={() => {
//                                 addToAlbum();
//                                 // getAlbumSongs()
//                             }}>Add to Album</button>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         </>
//     )
// }

// export default AlbumDetails;
