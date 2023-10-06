import React, { useState } from 'react';
import UpdatePlaylistModal from '../UpdatePlaylistModal/UpdatePlaylistModal';
import "./UpdatePlaylist.css"

const UpdatePlaylist = () => {

    const [showUpdateModal, setShowUpdateModal] = useState(false);
    const [playlistToUpdate, setPlaylistToUpdate] = useState(null)

    const handleOpenUpdateModal = (playlist) => {
        setPlaylistToUpdate(playlist);
        setShowUpdateModal(true)
    }

    const handleCloseUpdateModal = () => {
        setShowUpdateModal(false);
        setPlaylistToUpdate(null)
    }

    return (
        <>
            {showUpdateModal && (
                <UpdatePlaylistModal
                    onClose={handleCloseUpdateModal}
                />
            )}
        </>
    );
}

export default UpdatePlaylist
