import React, { useState } from 'react'
import DeletePlaylistModal from '../DeletePlaylistModal/DeletePlaylistModal'


function DeletePlaylist({playlistId}) {

    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [playlistToDelete, setPlaylistToDelete] = useState(null)

    const handleOpenDeleteModal = (playlist) => {
        setPlaylistToDelete(playlist);
        setShowDeleteModal(true)
    }

    const handleCloseDeleteModal = () => {
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
