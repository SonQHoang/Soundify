import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { getUserPlaylist } from "../../store/playlists"
import { NavLink } from 'react-router-dom';
import "./UserPlaylist.css"

const UserPlaylist = () => {
    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const playlist = (useSelector(state => state.playlist.allPlaylists))
    const userPlaylist = Object.values(playlist)

    console.log('userPlaylists Image=========>', userPlaylist)

    useEffect(() => {
        console.log("I'm dispatching getUserPlaylist")
        dispatch(getUserPlaylist())
    }, [dispatch, userId])


    return (
        <div className="playlist-container">
            {userPlaylist && userPlaylist.map(playlist => (

                <div key={playlist.id} className="individual-playlist-map">
                    <NavLink to={`/playlist/${playlist.id}`} className="link-no-underline">
                        <div className="individual-playlist-container">
                            <div className="playlist-icon-container">
                                <img src={playlist.image} className="playlist_image"></img>
                            </div>
                            <div className="playlist-info-container">
                                <div className="playlist-info-top">
                                    <p>{playlist.title}</p>
                                </div>
                                <div className="playlist-info-bottom">
                                    <p>Playlist or Album</p>
                                    <p> . </p>
                                    <p># Songs</p>
                                </div>
                            </div>
                        </div>
                        {/* <p>{playlist.owner}</p> */}
                    </NavLink>
                </div>
            ))}
        </div>
    );
}


export default UserPlaylist