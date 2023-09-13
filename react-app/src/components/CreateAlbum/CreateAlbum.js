import { useHistory } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createAlbum } from '../../store/albums';
import "./CreateAlbum.css" 

const CreateAlbum = () => {
    const dispatch = useDispatch()
    const history = useHistory();
    const currentUser = useSelector((state) => state.session.user)
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('')
    const [description, setDescription] = useState("")
    const [date_created, setDateCreated] = useState('');
    const [year, setYear] = useState('')
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
        if (validationErrors.length) return alert("You've got some errors with your upload!");
        const formData = new FormData()
        // formData.append("audio", audio)
        // console.log('What does audio give us back=======> The filename', audio)
        // formData.append('user_id', currentUser.id)
        formData.append('author', currentUser.first_name)
        // console.log('What does author gives us back======>', currentUser)
        formData.append('title', title)
        formData.append('photo', image)
        formData.append('album_description', description)
        formData.append('year', year)
        formData.append('date_created', date_created)

        // Confirming my data is in the form

        const formDataObject = {};
        formData.forEach((value, key) => {
            formDataObject[key] = value;
        });
        console.log('formDataObject:', formDataObject);

        try {
            await dispatch(createAlbum(formData));
            setValidationErrors([]);
            setHasSubmitted(false);
            history.push(`/`);
        } catch (error) {
            console.error("Error creating playlist:", error);
        }
    };

    return (
        <div className="create-playlist-container">

            <form className="create-playlist-form-container"
                onSubmit={(e) => submitForm(e)}
                encType="multipart/form-data"
            >
                <div className="form-input-box">
                    <div>
                        <label
                            className="form-label"
                            htmlFor='audio'
                        >
                            Add a Song:
                        </label>
                    </div>
                </div>
                <div className="form-input-box">
                    <div>
                        <label className="form-label" htmlFor='title'>
                            Album Title:
                        </label>
                    </div>
                    <div>
                        <input id="title" type="text" onChange={(e) => setTitle(e.target.value)} value={title} />
                    </div>
                </div>
                <div className="form-input-box">
                    <div>
                        <label className="form-label" htmlFor='title'>
                            Description:
                        </label>
                    </div>
                    <div>
                        <textarea id="title" type="text" onChange={(e) => setDescription(e.target.value)} value={description} />
                    </div>
                </div>
                <div className="form-input-box">
                    <div>
                        <label className="form-label" htmlFor='title'>
                            Year:
                        </label>
                    </div>
                    <div>
                        <textarea id="title" type="text" onChange={(e) => setYear(e.target.value)} value={year} />
                    </div>
                </div>
                <div>
                    <label className="form-label" htmlFor="image">
                        Upload an Album Cover:
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
                                <img src={imagePreview} alt="Playlist Image" width="100"/>
                        </div>
                    )}
                </div>
                <div className="form-input-box">
                    <div>
                        <label className="form-label" htmlFor='date_created'>
                            Date Created:
                        </label>
                    </div>
                    <div>
                        <input id="date_created" type="date" onChange={(e) => setDateCreated(e.target.value)} value={date_created} />
                    </div>
                </div>
                <div>
                    <button className="button">Submit</button>
                </div>
            </form>
        </div>
    );
}

export default CreateAlbum
