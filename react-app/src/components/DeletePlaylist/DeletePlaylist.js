import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import DeletePlaylistModal from '../DeletePlaylistModal/DeletePlaylistModal'


function DeletePlaylist({playlistId}) {
    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null)
    const dispatch = useDispatch()

    const handleOpenDeleteModal = (playlist) => {
        console.log('Opening Delete Modal');
        setPlaylistToDelete(playlist);
        setShowDeleteModal(true)
    }

    const handleCloseDeleteModal = () => {
        console.log('Closing Delete Modal');
        setShowDeleteModal(false);
        setPlaylistToDelete(null)
    }


    return (
        <>
            {showDeleteModal && (
                <DeletePlaylistModal
                    onClose={handleCloseDeleteModal}
                />
            )}
        </>
    );
}

export default DeletePlaylist
