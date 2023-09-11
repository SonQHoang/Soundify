import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { getUserPlaylist } from "../../store/playlists"
import { Link } from 'react-router-dom';
import "./UserPlaylist.css"

const UserPlaylist = () => {
    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const userPlaylist = Object.values(useSelector(state => state.playlist.allPlaylists))
    console.log('userPlaylists=========>', userPlaylist)

    useEffect(() => {
        console.log("I'm dispatching getUserPlaylist")
        dispatch(getUserPlaylist())
    }, [dispatch, userId])


    return (
        <>
            <div className="playlist-container">
                {userPlaylist.map(playlist => (
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


export default UserPlaylist