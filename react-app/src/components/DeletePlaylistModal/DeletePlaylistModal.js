import React, { useEffect, useRef } from 'react'
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
// import { GetSinglePlaylist } from '../../store/playlists';
import { DeletePlaylistThunk, getUserPlaylist } from '../../store/playlists';
import "./DeletePlaylistModal.css"

const DeletePlaylistModal = ({ onSubmit, onClose, playlistId }) => {
    const history = useHistory()

    const modalOverlayRef = useRef();
    const dispatch = useDispatch()

    const handleClickOutside = (e) => {
        if (modalOverlayRef.current === e.target) {
            onClose();
        }
    }

    useEffect(() => {
        document.addEventListener('mousedown', handleClickOutside)
        return () => {
            document.removeEventListener('mousedown', handleClickOutside)
        }
    }, [])

    const handleConfirmDelete = async () => {
            dispatch(DeletePlaylistThunk(playlistId))
            .then(() => dispatch(getUserPlaylist()))
            onSubmit();
            history.push('/landing-page')
    };

    return (
        <>
            <div className='delete-modal-backdrop'></div>
            <div className="delete-modal-overlay" ref={modalOverlayRef}>
                <div className="delete-modal-content">
                    <h2>Delete from Your Library</h2>
                    <p>This will delete this playlist from your library.</p>
                    <div className="delete-modal-buttons">
                        <button
                            className="cancel-button"
                            onClick={onClose}>
                            Cancel
                        </button>
                        <button
                            className="delete-button"
                            onClick={handleConfirmDelete}>
                            Delete
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default DeletePlaylistModal
