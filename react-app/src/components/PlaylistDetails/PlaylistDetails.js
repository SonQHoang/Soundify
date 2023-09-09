import { useSelector, useDispatch } from 'react-redux'
import './PlaylistDetails.css'
import { useState, useEffect } from 'react'
import { getAllSongs } from '../../store/songs'
import Song from '../Songs/Song'

function PlaylistDetails() {
    const dispatch = useDispatch()
    const [query, setQuery] = useState("") // Initialize query with an empty string

    useEffect(() => {
        // console.log("I'm dispatching getAllSongs")
        dispatch(getAllSongs())
    }, [dispatch])

    const songLibrary = Object.values(useSelector(state => state.songs.allSongs))
    // console.log('songLibrary=======>', songLibrary)

    const titleKVPairs = songLibrary.map(song => ({ title: song.title }));
    // console.log('titleKeyValuePairs=======>', titleKVPairs);

    const queryFilter = (query,titleKVPairs) => {
        if(!query) {
            return []
        }
        return titleKVPairs.filter(song => song.title.includes(query))
    }

    const filteredSongs = queryFilter(query, titleKVPairs)


    return (
        <>
            <h1>My Playlist #</h1>
            <div>
                <input
                    type="text"
                    placeholder="Search for a song"
                    onChange={(e) => setQuery(e.target.value)}
                />
            </div>
            <div className="playlist-details-container">
                <div>#</div>
                <div>Title</div>
                <div>Album</div>
                <div>Date Added</div> 
                <div></div>
                <div>Time Symbol</div>
            </div>
            <div className='search-bar'>
            {filteredSongs.map(value => <p key={value.title}>{value.title}</p>)}
            </div>
        </>
    )
}

export default PlaylistDetails