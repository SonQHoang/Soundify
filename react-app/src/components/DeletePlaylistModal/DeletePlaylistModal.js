import React, { useEffect, useRef } from 'react'
import { useDispatch } from 'react-redux';
// import { GetSinglePlaylist } from '../../store/playlists';
import { DeletePlaylistThunk, getUserPlaylist } from '../../store/playlists';
import "./DeletePlaylistModal.css"

const DeletePlaylistModal = ({ onSubmit, onClose, playlistId }) => {
    console.log('Delete Modal playlistId======>', playlistId)

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
        console.log('Delete button pressed');
        dispatch(DeletePlaylistThunk(playlistId))
        .then(() => dispatch(getUserPlaylist()))
            // .then(() => dispatch(GetSinglePlaylist()))
            // .then(() => {
                // console.log('DeletePlaylistThunk and GetSinglePlaylist dispatched');
                // onSubmit();
            // }
            // );
            onSubmit()
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
                            onClick={handleConfirmDelete}>
                            Cancel
                        </button>
                        <button
                            className="delete-button"
                            onClick={onClose}>
                            Delete
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default DeletePlaylistModal
