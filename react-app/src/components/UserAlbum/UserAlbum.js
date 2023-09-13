import { useDispatch, useSelector } from 'react-redux';
import { useEffect } from 'react';
import { getUserAlbum } from '../../store/albums';
import { Link } from 'react-router-dom';
import "./UserAlbum.css"

const UserAlbum = () => {
    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    const userId = sessionUser.id

    const album = (useSelector(state => state.album.allAlbums))
    console.log('album useralbum component=========>', album)
    
    const userAlbum = Object.values(album)

    // console.log('userPlaylists=========>', userPlaylist)

    useEffect(() => {
        // console.log("I'm dispatching getUserPlaylist")
        dispatch(getUserAlbum())
    }, [dispatch, userId])


    return (
        <>
            <div className="album-container">
                {userAlbum && userAlbum.map(album => (
                    <div key={album.id} className="individual-album">
                        <Link to={`/album/${album.id}`} className="link-no-underline">
                            <p>{album.title}</p>
                            <p>{album.owner}</p>
                        </Link>
                    </div>
                ))}
            </div>
        </>
    );
}


export default UserAlbum