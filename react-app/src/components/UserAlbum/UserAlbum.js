import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { getUserAlbum } from '../../store/albums';
import { NavLink } from 'react-router-dom';
import "./UserAlbum.css"

const UserAlbum = () => {
    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const album = (useSelector(state => state.album.allAlbums))

    const userAlbum = Object.values(album)


    useEffect(() => {
        dispatch(getUserAlbum())
    }, [dispatch, userId])


    return (
        <div className="album-container">
            {userAlbum && userAlbum.map(album => (
                <div key={album.id} className="individual-album-map">
                    <NavLink to={`/album/${album.id}`} className="link-no-underline">

                        <div className="individual-album-container">
                            <div className="album-icon-container">
                                <img src={album.album_photo} className="album-photo" alt="album cover"></img>
                            </div>
                            <div className="album-info-container">
                                <div className="album-info-top">
                                    <p>{album.title}</p>
                                </div>
                                <div className="album-info-bottom">
                                    <p>Album</p>
                                    <p></p>
                                    <p></p>
                                </div>
                            </div>
                        </div>
                    </NavLink>
                </div>
            ))}
        </div>
    );
}


export default UserAlbum