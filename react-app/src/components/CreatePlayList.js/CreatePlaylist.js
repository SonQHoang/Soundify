import { useHistory } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createPlaylist } from '../../store/playlists';
import "./CreatePlaylist.css"

const CreatePlaylist = () => {
    const dispatch = useDispatch()
    const history = useHistory();
    const currentUser = useSelector((state) => state.session.user.first_name)

    const [audio, setAudio] = useState(null);
    const [validationErrors, setValidationErrors] = useState([])
    const [hasSubmitted, setHasSubmitted] = useState(false)

    useEffect(() => {
        const errors = [];
        if (!audio) errors.push("Please provide an audio file!")
        setValidationErrors(errors);
    }, [audio])

    const submitForm = async (e) => {
        e.preventDefault();

        setHasSubmitted(true);
        if (validationErrors.length) return alert("You've got some errors with your upload!");

        const formData = new FormData()
        formData.append("audio", audio)
        formData.append('author', currentUser.id)

        try {
            await dispatch(createPlaylist(formData));
            setValidationErrors([]);
            setHasSubmitted(false);
            history.push("/albums");
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
                            Upload Song:
                        </label>
                    </div>
                    <div>
                        <input
                            id="audio"
                            type="file"
                            accept="audio/*"
                            onChange={(e) => setAudio(e.target.files[0])}
                        />
                    </div>
                </div>
                <div>
                    <button className="button">Submit</button>
                </div>
            </form>
        </div>
    );
}

export default CreatePlaylist
