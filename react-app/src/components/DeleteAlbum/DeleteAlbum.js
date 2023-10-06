import React, { useState } from 'react'
import DeleteAlbumModal from '../DeleteAlbumModal/DeleteAlbumModal'

function DeleteAlbum({albumId}) {

    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [albumToDelete, setAlbumToDelete] = useState(null)

    const handleOpenDeleteModal = (album) => {
        setAlbumToDelete(album);
        setShowDeleteModal(true)
    }

    const handleCloseDeleteModal = () => {
        setShowDeleteModal(false);
        setAlbumToDelete(null)
    }


    return (
        <>
            {showDeleteModal && (
                <DeleteAlbumModal
                    onClose={handleCloseDeleteModal}
                />
            )}
        </>
    );
}

export default DeleteAlbum
