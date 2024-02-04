import { useHistory } from 'react-router-dom';
import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createPlaylist } from '../../store/playlists';
import "./CreatePlaylist.css"

// This component contains the form data to create a new customized playlist
const CreatePlaylist = () => {
    const dispatch = useDispatch()
    const history = useHistory();
    const currentUser = useSelector((state) => state.session.user)

    const [title, setTitle] = useState('');
    const [image, setImage] = useState(null)
    const [description, setDescription] = useState("")
    const [date_created, setDateCreated] = useState('');
	const [errors, setErrors] = useState([]);
    const [imagePreview, setImagePreview] = useState(null)
    const [hasSubmitted, setHasSubmitted] = useState(false) 


    const submitForm = async (e) => {
        e.preventDefault();

        const newErrors = {}

        if(!title) {
            newErrors.title = "Playlist title is required"
        } else if (title.length > 15) {
            newErrors.title = "Please submit a playlist title that is less than 15 characters long"
        } else if (title.length <= 5) {
            newErrors.title = "Playlist title must be at least 5 character long"
        }

        if(!description) {
            newErrors.description = "Description is required"
        } else if (description.length <= 15) {
            newErrors.description = "Description must be at least 10 characters long"
        } else if (description.length >= 30) {
            newErrors.description = "Description cannot exceed 25 characters in length"
        }

        if (!image) {
            newErrors.image = "Playlist image is required"
        }

        if (!date_created) {
            newErrors.date_created = "You must submit a date for your playlist"
        }

        setErrors(newErrors)
        setHasSubmitted(true);

        if(Object.keys(newErrors).length === 0) {
            const formData = new FormData()
            formData.append('author', currentUser.first_name)
            formData.append('title', title)
            formData.append('image', image)
            formData.append('playlist_description', description)
            formData.append('date_created', date_created)
    
            try {
                await dispatch(createPlaylist(formData));
                setErrors({});
                setHasSubmitted(false);
                history.push(`/landing-page`);
            } catch (error) {
                console.error("Error creating playlist:", error);
            }
        }
    };


    return (
        <div className="create-playlist-container">

            <form className="create-playlist-form-container"
                onSubmit={(e) => submitForm(e)}
                encType="multipart/form-data"
            >
                <h1>Create a New Playlist</h1>
                <div className="form-input-box">
                    <div>
                    <div className="error-message">{errors.title}</div>
                        <label className="form-label" htmlFor='title'>
                            Playlist Title:
                        </label>
                    </div>
                    <div>
                        <input id="title" type="text" onChange={(e) => setTitle(e.target.value)} value={title} />
                    </div>
                </div>
                <div className="form-input-box">
                    <div>
                    <div className="error-message">{errors.description}</div>
                        <label className="form-label" htmlFor='title'>
                            Description:
                        </label>
                    </div>
                    <div>
                        <textarea id="title" type="text" onChange={(e) => setDescription(e.target.value)} value={description} />
                    </div>
                </div>
                <div className="form-input-box">
                <div className="error-message">{errors.image}</div>
                    <label className="form-label" htmlFor="image">
                        Upload a Picture:
                    </label>
                    <input
                        id="image"
                        type="file"
                        name="image"
                        accept="image/*"
                        onChange={(e) => {
                            setImage(e.target.files[0]);
                            if (e.target.files[0]) {
                                const url = URL.createObjectURL(e.target.files[0]);
                                setImagePreview(url);
                            } else {
                                setImagePreview(null);
                            }
                        }}
                    />
                    {imagePreview && (
                        <div>
                            <img src={imagePreview} alt="Playlist Image" width="100" />
                        </div>
                    )}
                </div>
                <div className="form-input-box">
                    <div>
                    <div className="error-message">{errors.date_created}</div>
                        <label className="form-label" htmlFor='date_created'>
                            Date Created:
                        </label>
                    </div>
                    <div>
                        <input id="date_created" type="date" onChange={(e) => setDateCreated(e.target.value)} value={date_created} />
                    </div>
                </div>
                <div>
                    <button className="playlist-create-submit-button">Submit</button>
                </div>
            </form>
        </div>
    );
}

export default CreatePlaylist
