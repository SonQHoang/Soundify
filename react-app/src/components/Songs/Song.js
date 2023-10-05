import React, {useState} from "react"
import { useDispatch, useSelector } from 'react-redux';
import { getAllSongs } from "../../store/songs";
import { useEffect } from "react";
import Player from "../AudioBar/audiobar";

const Song = () => {
    const dispatch = useDispatch()

    const allSongs = Object.values(useSelector(state => state.songs.allSongs))

    const [selectedSongUrl, setSelectedSongUrl] = useState(null)

    useEffect(() => {
        dispatch(getAllSongs())
    }, [dispatch]);

    return (
        <>
        <h1>Song Library</h1>
        {selectedSongUrl && <Player src={selectedSongUrl}/>}
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