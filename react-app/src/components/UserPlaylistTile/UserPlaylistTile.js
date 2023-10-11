import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect} from 'react';
import { getUserPlaylist } from '../../store/playlists';
import { NavLink} from 'react-router-dom';
import "./UserPlaylistTile.css";

const UserPlaylistTile = () => {
  const dispatch = useDispatch();
  const playlists = useSelector(state => state.playlist.allPlaylists);
  useEffect(() => {
    dispatch(getUserPlaylist());
  }, []);

  return (
    <div className='playlist-tile-wrapper'>
        {Object.values(playlists).map(playlist => (
          <NavLink to={`/playlist/${playlist.id}`}>
          <div key={playlist.id} className="playlist-tile-container">
            <img src={playlist.image} className="playlist-image-tile" alt="playlist cover" />
            <div className="playlist-info-wrapper">
              <div className="playlist-info">
                <p>{playlist.title}</p>
                <p>{playlist.description}</p>
              </div>
            </div>
          </div>
          </NavLink>
        ))}
    </div>
  );
};

export default UserPlaylistTile;