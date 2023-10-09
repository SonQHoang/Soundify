import React, { useEffect, useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom'
import { updateAlbumThunk, GetSingleAlbum } from '../../store/albums';

import "./UpdateAlbumModal.css"

const UpdateAlbumModal = ({ onSubmit, onClose, albumId }) => {
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

    //==========================ModalLogic End================================

    //===========================Update Form Start===================================
    const current_album_information = useSelector(state => state.album.singleAlbum)

    const [title, setTitle] = useState(current_album_information.title || '');
    const [year, setYear] = useState(current_album_information.year || '')
    const [album_description, setAlbum_Description] = useState(current_album_information.album_description || "")
    const [errors, setErrors] = useState([]);
    const [album_photo, setAlbum_Photo] = useState(current_album_information.album_photo || '')
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [imagePreview, setImagePreview] = useState(null)
    const [albumInformation, setAlbumInformation] = useState(current_album_information)

    useEffect(() => {
        setAlbumInformation(current_album_information)
    }, [albumInformation])


    const submitForm = async (e) => {
        e.preventDefault();

        const newErrors = {}

        if (!title) {
            newErrors.title = "Album title cannot be empty"
        } else if (title.length > 15) {
            newErrors.title = "Updated album title must be less than 15 characters long"
        } else if (title.length <= 0) {
            newErrors.title = "Updated album title must be at least 1 character long"
        }

        if (!album_description) {
            newErrors.album_description = "Description cannot be empty"
        } else if (album_description.length <= 15) {
            newErrors.album_description = "Updated description must be at least 15 characters long"
        } else if (album_description.length >= 30) {
            newErrors.album_description = "Updated description cannot exceed 40 characters in length"
        }

        if (!year) {
            newErrors.year = "Year is required"
        } else if (isNaN(year) || parseInt(year) <= 0) {
            newErrors.year = "Year must be a positive number greater than 0"
        }

        if (!album_photo) {
            newErrors.album_photo = "Album Cover is required"
        }

        setErrors(newErrors)
        setHasSubmitted(true);

        if (Object.keys(newErrors).length === 0) {
            const formData = new FormData()
            formData.append('author', currentUser.first_name)
            formData.append('title', title)
            formData.append('year', year)
            formData.append('album_photo', album_photo)
            formData.append('album_description', album_description)

            try {
                await dispatch(updateAlbumThunk(albumId, formData))

                await dispatch(GetSingleAlbum(albumId)) // Triggering the rerender
                onSubmit();
                history.push(`/album/${albumId}`)
            } catch (error) {
                console.error("Error while updating album:", error);
            }

        }
    }
    //==========================UpdateFormEnd===============================


    return (
        <>
            <div className='update-modal-backdrop'></div>
            <div className="update-modal-overlay" ref={modalOverlayRef}>
                <div className="update-modal-content">
                    <div className="update-modal-h2">
                        <h2>Edit Details</h2>
                    </div>
                    <div className="update-album-container">
                        <form className="update-album-form-container"
                            onSubmit={(e) => submitForm(e)}
                            encType="multipart/form-data"
                        >
                            <div className="update-form-left-side">
                                <div className="error-message">{errors.album_photo}</div>
                                <label className="form-label" htmlFor="image">
                                    Update Your Album Cover:
                                </label>
                                <input
                                    id="image"
                                    type="file"
                                    name="image"
                                    accept="image/*"
                                    onChange={(e) => {
                                        setAlbum_Photo(e.target.files[0]);
                                        if (e.target.files[0]) {
                                            const url = URL.createObjectURL(e.target.files[0]);
                                            setImagePreview(url);
                                        } else {
                                            setImagePreview(null);
                                        }
                                    }}
                                />
                                {album_photo && (
                                    <div>
                                        <img src={album_photo} alt="Album Image" width="100" />
                                    </div>
                                )}
                            </div>
                            <div className="update-form-right-side">
                                <div className="form-input-box">
                                        <div className="error-message">{errors.title}</div>
                                        <label>
                                            Title:
                                        </label>
                                    <div>
                                        <input
                                            className="input-field"
                                            id="title"
                                            type="text"
                                            name="title" // Add the name attribute here
                                            onChange={(e) => setTitle(e.target.value)}
                                            value={title}
                                        />
                                    </div>
                                </div>
                                <div className="form-input-box">
                                    <div>
                                        <div className="error-message">{errors.album_description}</div>
                                        <label className="form-label" htmlFor='description'>
                                            Description:
                                        </label>
                                    </div>
                                    <div>
                                        <textarea
                                            className="input-field"
                                            id="description"
                                            name="album_description" // Add the name attribute here
                                            type="text"
                                            onChange={(e) => setAlbum_Description(e.target.value)}
                                            value={album_description}
                                        />
                                    </div>
                                </div>
                                <div className="form-input-box">
                                    <div>
                                        <div className="error-message">{errors.year}</div>
                                        <label className="form-label" htmlFor='year'>
                                            Year
                                        </label>
                                    </div>
                                    <div>
                                        <input
                                            className="input-field"
                                            id="year"
                                            name="year"
                                            type="number"
                                            onChange={(e) => setYear(e.target.value)}
                                            value={year}
                                        />
                                    </div>
                                </div>

                            </div>
                        </form>
                    </div>
                    <div className="update-modal-buttons">
                        <button
                            className="update-button"
                            onClick={submitForm}>
                            Save
                        </button>
                    </div>
                    {/* <div className="disclaimer-text">
                        By proceeding, you agree to give Soundify access to the image you choose to upload. Please make sure you have the right to upload the image.
                    </div> */}
                </div>
            </div>
        </>
    );
};

export default UpdateAlbumModal
