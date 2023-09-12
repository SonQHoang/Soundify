import React, { useEffect, useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { UpdatePlaylistThunk, getUserPlaylist } from '../../store/playlists';

import "./UpdatePlaylistModal.css"

const UpdatePlaylisttModal = ({ onSubmit, onClose, playlistId }) => {
    // console.log('Delete Modal playlistId======>', playlistId)
    const history = useHistory()
    const currentUser = useSelector((state) => state.session.user)

    //========================Modal Logic Start==================
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

    const handleConfirmUpdate = async () => {
        dispatch(UpdatePlaylistThunk(playlistId))
            .then(() => dispatch(getUserPlaylist())) // Triggering the rerender
        onSubmit();
        history.push(`/playlist/${playlistId}`)
    };

    //==========================ModalLogic End================================

    //===========================Update Form Start===================================
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('')
    const [description, setDescription] = useState("")
    const [validationErrors, setValidationErrors] = useState([])
    const [imagePreview, setImagePreview] = useState(null)
    const [hasSubmitted, setHasSubmitted] = useState(false)


    const handleImageUpload = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                setImagePreview(e.target.result)
                console.log('Uploaded Image Data:======>', e.target.result);
            }
            reader.readAsDataURL(file)
        } else {
            console.log("No image was uploaded")
        }
    }

    const submitForm = async (e) => {
        e.preventDefault();

        setHasSubmitted(true);
        if (validationErrors.length) return alert("You've got some errors with your edit!");
        const formData = new FormData()

        formData.append('author', currentUser.first_name)
        formData.append('title', title)
        formData.append('photo', image)
        formData.append('description', description)

        // Confirming my data is in the form

        const formDataObject = {};
        formData.forEach((value, key) => {
            formDataObject[key] = value;
        });
        console.log('formDataObject:', formDataObject);
    };

    //==========================UpdateFormEnd===============================


    return (
        <>
            <div className='update-modal-backdrop'></div>
            <div className="update-modal-overlay" ref={modalOverlayRef}>
                <div className="update-modal-content">
                    <div className="update-modal-h2">
                        <h2>Edit Details</h2>
                    </div>
                    <div className="update-playlist-container">
                        <form className="update-playlist-form-container"
                            onSubmit={(e) => submitForm(e)}
                            encType="multipart/form-data"
                        >
                            <div className="update-form-left-side">
                                <label className="form-label" htmlFor="image">
                                    Adjust Your Picture:
                                </label>
                                <input
                                    id="image"
                                    type="file"
                                    name="image"
                                    accept="image/*"
                                    onChange={handleImageUpload}
                                />
                                {imagePreview && (
                                    <div>
                                        <img src={imagePreview} alt="Playlist Image" width="100" />
                                    </div>
                                )}
                            </div>
                            <div className="update-form-right-side">
                                <div className="form-input-box">
                                    <div>
                                        <input className="input-field" id="title" type="text" onChange={(e) => setTitle(e.target.value)} value={title} />
                                    </div>
                                </div>
                                <div className="form-input-box">
                                    <div>
                                        <label className="form-label" htmlFor='description'>
                                            Description (Optional):
                                        </label>
                                    </div>
                                    <div>
                                        <textarea className="input-field" id="title" type="text" onChange={(e) => setDescription(e.target.value)} value={description} />
                                    </div>
                                </div>
                                <div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div className="update-modal-buttons">
                        <button
                            className="update-button"
                            onClick={handleConfirmUpdate}>
                            Save
                        </button>
                    </div>
                    <div className="disclaimer-text">
                        By proceeding, you agree to give Soundify access to the image you choose to upload. Please make sure you have the right to upload the image.
                    </div>
                </div>
            </div>
        </>
    );
};

export default UpdatePlaylisttModal
