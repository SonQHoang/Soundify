import React, {useState} from "react"
import { useDispatch, useSelector } from 'react-redux';
import { getAllSongs } from "../../store/songs";
// import { NavLink } from "react-router-dom"
import { useEffect } from "react";
import Player from "../AudioBar/audiobar";

const Song = () => {
    // const [songs, setSongs] = useState([])
    const dispatch = useDispatch()

    const allSongs = Object.values(useSelector(state => state.songs.allSongs))
    console.log('allSongs=========>', allSongs)

    const [selectedSongUrl, setSelectedSongUrl] = useState(null)
    console.log('selectedSongUrl=========>', selectedSongUrl)
    
    useEffect(() => {
        console.log('Dispatching getAllSongs');
        dispatch(getAllSongs())
    }, [dispatch]);


    // const playSong = (song) => {
    //     console.log('Calling playSong function called');
    //     console.log('What is the song=======>', song)
    //     setSelectedSongUrl(song.url)
    // }

    return (
        <>
        <h1>Song Library</h1>
        {selectedSongUrl && <Player src={selectedSongUrl} />}
        <div className="song-container">
            {allSongs.map(song => (
                <div key={song.id}>
                    <p onClick={() => setSelectedSongUrl(song.audio_url)}>{song.title}</p>
                </div>
            ))}
        </div>
        </>
    )
}

export default Song