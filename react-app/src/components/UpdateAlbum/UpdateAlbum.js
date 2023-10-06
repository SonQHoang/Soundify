import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import UpdateAlbumModal from '../UpdateAlbumModal/UpdateAlbumModal';
import "./UpdateAlbum.css"

const UpdateAlbum = () => {
    const dispatch = useDispatch() 

    const [showUpdateModal, setShowUpdateModal] = useState(false);
    const [albumToUpdate, setAlbumToUpdate] = useState(null)

    const handleOpenUpdateModal = (playlist) => {
        setAlbumToUpdate(playlist);
        setShowUpdateModal(true)
    }

    const handleCloseUpdateModal = () => {
        setShowUpdateModal(false);
        setAlbumToUpdate(null)
    }

    return (
        <>
            {showUpdateModal && (
                <UpdateAlbumModal
                    onClose={handleCloseUpdateModal}
                />
            )}
        </>
    );
}

export default UpdateAlbum
