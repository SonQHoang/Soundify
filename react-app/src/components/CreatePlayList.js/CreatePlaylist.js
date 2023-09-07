// import { useHistory } from 'react-router-dom';
// import { useEffect } from 'react';

// const CreatePlaylist = () => {
//     const dispatch = useDispatch()
//     const history = useHistory();
//     const currentUser = useSelector((state) => state.euserState.currentUser)

//     const submitForm = async (e) => {
//         e.preventDefault();

//         setHasSubmitted(true);
//         if (validationErrors.length) return alert("You've got some errors with your upload!");

//         const formData = new FormData()
//         formData.append("audio", audio)
//         formData.append('author', currentUser.id)

//         try {
//             await dispatch(createPlaylist(formData));
//             setCaption("");
//             setImage("");
//             setValidationErrors([]);
//             setHasSubmitted(false);
//             history.push("/albums");
//         } catch (error) {
//             console.error("Error creating playlist:", error);
//         }

//         useEffect(() => {
//             const errors = [];
//             if (!audio) errors.push("Please provide an audio file!")
//             setValidationErrors(errors);
//         }, [audio])
//     };

//     return (
//         <>
//             <form
//                 onSubmit={(e) => submitForm(e)}
//                 encType="multipart/form-data"
//             >
//                 <div className="form-input-box">
//                     <label
//                         className="form-label"
//                         htmlFor='audio'
//                     >
//                         Upload Song:
//                     </label>
//                     <input
//                         id="audio"
//                         type="file"
//                         accept="audio/*"
//                         onChange={(e) => setAudio(e.target.files[0])}
//                     />
//                 </div>
//                 <button className="button">Submit</button>
//             </form>
//         </>
//     );
// }

// export default CreatePlaylist
