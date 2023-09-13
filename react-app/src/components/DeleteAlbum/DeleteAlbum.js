import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import DeleteAlbumModal from '../DeleteAlbumModal/DeleteAlbumModal'

function DeleteAlbum({albumId}) {
    const dispatch = useDispatch()   

    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [albumToDelete, setAlbumToDelete] = useState(null)

    const handleOpenDeleteModal = (album) => {
        console.log('Opening Delete Modal');
        setAlbumToDelete(album);
        setShowDeleteModal(true)
    }

    const handleCloseDeleteModal = () => {
        console.log('Closing Delete Modal');
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
