import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import './Playlist.css';
import { getAllPlaylists } from '../../store/playlists';
import { Link } from 'react-router-dom';

const Playlist = () => {
    const dispatch = useDispatch()


    const allPlaylists = Object.values(useSelector(state => state.playlist.allPlaylists))
    console.log('allplaylists=========>', allPlaylists)

    useEffect(() => {
        dispatch(getAllPlaylists())
    }, [dispatch])


    return (
        <>
            <div className="playlist-container">
                {allPlaylists.map(playlist => (
                    <div key={playlist.id} className="individual-playlist">
                        <Link to={`/playlist/${playlist.id}`} className="link-no-underline">
                            <p>{playlist.title}</p>
                            <p>{playlist.owner}</p>
                        </Link>
                    </div>
                ))}
            </div>
        </>
    );
}

export default Playlist


