import { useHistory } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom/';
import { useDispatch, useSelector } from 'react-redux';
import { createAlbum } from '../../store/albums';
import "./CreateAlbum.css" 

const CreateAlbum = () => {
    const dispatch = useDispatch()
    const history = useHistory();
    const currentUser = useSelector((state) => state.session.user)
    const [title, setTitle] = useState('');
    const [album_photo, setAlbum_Photo] = useState('')
    // console.log('setAlbum_Photo=======>', setAlbum_Photo)
    const [description, setDescription] = useState("")
    const [date_created, setDateCreated] = useState('');
    const [year, setYear] = useState('')
    const [validationErrors, setValidationErrors] = useState([])
    const [imagePreview, setImagePreview] = useState(null)
    const [hasSubmitted, setHasSubmitted] = useState(false)


    const submitForm = async (e) => {
        e.preventDefault();

        setHasSubmitted(true);
        if (validationErrors.length) return alert("You've got some errors with your upload!");
        const formData = new FormData()

        formData.append('author', currentUser.first_name)
        formData.append('title', title)
        formData.append('album_photo', album_photo)
        formData.append('album_description', description)
        formData.append('year', year)
        formData.append('date_created', date_created)

        // Confirming my data is in the form

        const formDataObject = {};
        formData.forEach((value, key) => {
            formDataObject[key] = value;
        });
        console.log('formDataObject=========> component:', formDataObject);

        try {
            await dispatch(createAlbum(formData));
            setValidationErrors([]);
            setHasSubmitted(false);
            history.push(`/landing-page`);
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
                <h1>Create a New Album</h1>
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
                        onChange={(e) => {
                            setAlbum_Photo(e.target.files[0]);
                            if (e.target.files[0]) {
                                const url = URL.createObjectURL(e.target.files[0]);
                                setImagePreview(url);
                            } else {
                                setImagePreview(null);
                            }
                        }}                    />
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
