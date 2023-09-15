import React, { useEffect, useRef } from 'react'
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
// import { GetSinglePlaylist } from '../../store/playlists';
import { deleteAlbumThunk, getUserAlbum } from '../../store/albums';
import "./DeleteAlbumModal.css"

const DeleteAlbumModal = ({ onSubmit, onClose, albumId }) => {
    // console.log('Delete Modal albumId======>', albumId)
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
            dispatch(deleteAlbumThunk(albumId))
            .then(() => dispatch(getUserAlbum())) // Triggering the rerender
            onSubmit();
            history.push('/landinge-page')
    };

    return (
        <>
            <div className='delete-album-modal-backdrop'></div>
            <div className="delete-album-modal-overlay" ref={modalOverlayRef}>
                <div className="delete-album-modal-content">
                    <h2>Delete from Your Library</h2>
                    <p>This will delete this Album from your library.</p>
                    <div className="delete-album-modal-buttons">
                        <button
                            className="cancel-button-album"
                            onClick={onClose}>
                            Cancel
                        </button>
                        <button
                            className="delete-button-album"
                            onClick={handleConfirmDelete}>
                            Delete
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default DeleteAlbumModal
