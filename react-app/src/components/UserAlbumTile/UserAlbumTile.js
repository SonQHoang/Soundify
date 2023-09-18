import React from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { getUserAlbum } from '../../store/albums';
import { NavLink } from 'react-router-dom';
import "./UserAlbumTile.css"; // Make sure to include the correct CSS file

const UserAlbumTile = () => {
    const history = useHistory();
    const dispatch = useDispatch();
    const albums = useSelector(state => state.album.allAlbums);
    console.log('What are my albums like?=====>', albums);

    useEffect(() => {
        dispatch(getUserAlbum());
    }, []);

    return (
        <div className='album-tile-wrapper'>
            {Object.values(albums).map(album => (
                <NavLink to={`/album/${album.id}`}>
                    <div key={album.id} className="album-tile-container">
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