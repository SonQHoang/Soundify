import React from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { getUserAlbum } from '../../store/albums';
import { NavLink } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import "./UserAlbumTile.css"; 

const UserAlbumTile = () => {
    const { id } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();
    const albums = useSelector(state => state.album.allAlbums);

    useEffect(() => {
        dispatch(getUserAlbum());
    }, []);


    return (
        <div className='album-tile-wrapper'>
            {Object.values(albums).map(album => (
                <NavLink key={album.id} to={`/album/${album.id}`}>
                    <div className="album-tile-container">
                        <img src={album.album_photo} className="album-image" alt="Logo" />
                        <div className="album-info-wrapper">
                            <div className="album-info">
                                <p>{album.title}</p>
                                <p>{album.description}</p>
                            </div>
                        </div>
                    </div>
                </NavLink>
            ))}
        </div>
    );
};

export default UserAlbumTile;