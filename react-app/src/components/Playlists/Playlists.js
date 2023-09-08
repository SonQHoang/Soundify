import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import './Playlist.css';
import { getAllPlaylists } from '../../store/playlists';

const Playlist = () => {
    const dispatch = useDispatch()


    const allPlaylists = Object.values(useSelector(state => state.playlist.allPlaylists))
    console.log('allPlaylists=======>', allPlaylists)
    const sessionuser = useSelector((state) => state.session.user)

    useEffect(() => {
        dispatch(getAllPlaylists())
    }, [dispatch])


    return (
        <>
            <div className="playlist-container">
                {allPlaylists.map(playlist => (
                    <div key={playlist.id} className="individual-playlist">
                        <p>{playlist.title}</p>
                        <p>{playlist.owner}</p>
                    </div>
                ))}

            </div>
        </>
    );
}

export default Playlist


{/* <div>#</div>
                <div>Title</div>
                <div>Album</div>
                <div>Date Added</div>
                <div></div>
                <div>Time Symbol</div> */}