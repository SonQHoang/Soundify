import { useHistory } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import UpdatePlaylistModal from '../UpdatePlaylistModal/UpdatePlaylistModal';
import "./UpdatePlaylist.css"

const UpdatePlaylist = () => {
    const dispatch = useDispatch()

    const [showUpdateModal, setShowUpdateModal] = useState(false);
    const [playlistToUpdate, setPlaylistToUpdate] = useState(null)

    const handleOpenUpdateModal = (playlist) => {
        console.log('Opening Update Modal');
        setPlaylistToUpdate(playlist);
        setShowUpdateModal(true)
    }

    const handleCloseUpdateModal = () => {
        console.log('Closing Update Modal');
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
