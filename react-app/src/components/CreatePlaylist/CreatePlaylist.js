import { useHistory } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { createPlaylist } from '../../store/playlists';
import "./CreatePlaylist.css"

const CreatePlaylist = () => {
    const dispatch = useDispatch()
    const history = useHistory();
    const currentUser = useSelector((state) => state.session.user.first_name)
    const [audioFileUrl, setAudioFileUrl] = useState('') // Storing audio files
    const [audio, setAudio] = useState(null);
    const [title, setTitle] = useState(''); 
    const [date_created, setDateCreated] = useState('');
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
        // console.log('What does audio give us back=======> The filename', audio)
        formData.append('author', currentUser)
        // console.log('What does author gives us back======>', currentUser)
        formData.append('title', title)
        formData.append('date_created', date_created)
        // Confirming my data is in the form
        // const formDataObject = {};
        // formData.forEach((value, key) => {
        //     formDataObject[key] = value;
        // });
        // console.log('formDataObject:', formDataObject);

        try {
            await dispatch(createPlaylist(formData));
            setValidationErrors([]);
            setHasSubmitted(false);
            // history.push("/playlist");
        } catch (error) {
            console.error("Error creating playlist:", error);
        }
    };

    const handleAudioChange = (e) => {
        const audio = e.target.files[0];
        console.log('Selected Audio Binary Data: ======>', audio);
        setAudio(audio)
        const url = URL.createObjectURL(audio);
        console.log('What is this url========>', url)
        setAudioFileUrl(url)
    }


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
                            Playlist Title:
                        </label>
                    </div>
                    <div>
                        <input id="title" type="text" onChange={(e) => setTitle(e.target.value)} value={title} />
                    </div>
                    <div>
                        <input
                            id="audio"
                            type="file"
                            accept="audio/*"
                            onChange={(e) => handleAudioChange(e)}
                        />
                    </div>
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
            {/* Confirmation on the correct file being submitted submitted */}
            {audioFileUrl && (
                <div className="audio-player">
                    <audio controls>
                        <source src={audioFileUrl} type="audio/mpeg" />
                    </audio>
                </div>
            )}
        </div>
    );
}

export default CreatePlaylist
