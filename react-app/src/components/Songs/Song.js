import React from "react"
import { useDispatch, useSelector } from 'react-redux';
import { getAllSongs } from "../../store/songs";
// import { NavLink } from "react-router-dom"
import { useEffect } from "react";

const Song = () => {
    // const [songs, setSongs] = useState([])
    const dispatch = useDispatch()

    const allSongs = Object.values(useSelector(state => state.songs.allSongs))
    console.log('allSongs=========>', allSongs)

    useEffect(() => {
        console.log('Dispatching getAllSongs');
        dispatch(getAllSongs())
    }, [dispatch]);

    return (
        <>
        <h1>Song Library</h1>
        <div className="song-container">
            {allSongs.map(song => (
                <div key={song.id}>
                    <p>{song.title}</p>
                </div>
            ))}
        </div>
        </>
    )
}

export default Song