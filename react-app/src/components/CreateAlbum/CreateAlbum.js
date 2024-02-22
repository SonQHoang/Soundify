import { useHistory } from "react-router-dom"
import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { createAlbum } from "../../store/albums"
import "./CreateAlbum.css"

// This component contains the form data needed to create a new album
// This is what I was tested on during a mock interview
const CreateAlbum = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const currentUser = useSelector((state) => state.session.user)
  const [title, setTitle] = useState("")
  const [album_photo, setAlbum_Photo] = useState("")
  const [description, setDescription] = useState("")
  const [date_created, setDateCreated] = useState("")
  const [year, setYear] = useState("")
  const [errors, setErrors] = useState([])
  const [imagePreview, setImagePreview] = useState(null)
  const [hasSubmitted, setHasSubmitted] = useState(false)

  const submitForm = async (e) => {
    e.preventDefault()

    const newErrors = {}

    if (!title) {
      newErrors.title = "Album title is required"
    } else if (title.length > 15) {
      newErrors.title =
        "Please submit an album title that is less than 15 characters long"
    } else if (title.length <= 0) {
      newErrors.title = "Album title must be at least 1 character long"
    }

    if (!description) {
      newErrors.description = "Description is required"
    } else if (description.length <= 15) {
      newErrors.description = "Description must be at least 15 characters long"
    } else if (description.length >= 30) {
      newErrors.description =
        "Description cannot exceed 40 characters in length"
    }

    if (!year) {
      newErrors.year = "Year is required"
    } else if (isNaN(year) || parseInt(year) <= 0) {
      newErrors.year = "Year must be a positive number greater than 0"
    }

    if (!album_photo) {
      newErrors.album_photo = "Album Cover is required"
    }

    if (!date_created) {
      newErrors.date_created = "You must submit a date for your album"
    }

    setErrors(newErrors)
    setHasSubmitted(true)

    if (Object.keys(newErrors).length === 0) {
      const formData = new FormData()
      formData.append("author", currentUser.first_name)
      formData.append("title", title)
      formData.append("album_photo", album_photo)
      formData.append("album_description", description)
      formData.append("year", year)
      formData.append("date_created", date_created)

      try {
        await dispatch(createAlbum(formData))
        setErrors({})
        setHasSubmitted(false)
        history.push(`/landing-page`)
      } catch (error) {
        console.error("Error creating album:", error)
      }
    }
  }

  return (
    <div className="create-album-container">
      <form
        className="create-album-form-container"
        onSubmit={(e) => submitForm(e)}
        encType="multipart/form-data"
      >
        <h1>Create a New Album</h1>
        <div className="form-input-box">
          <div>
            <div className="error-message">{errors.title}</div>
            <label className="form-label" htmlFor="title">
              Album Title:
            </label>
          </div>
          <div>
            <input
              id="title"
              type="text"
              onChange={(e) => setTitle(e.target.value)}
              value={title}
            />
          </div>
        </div>
        <div className="form-input-box">
          <div>
            <div className="error-message">{errors.description}</div>
            <label className="form-label" htmlFor="title">
              Description:
            </label>
          </div>
          <div>
            <textarea
              id="title"
              type="text"
              onChange={(e) => setDescription(e.target.value)}
              value={description}
            />
          </div>
        </div>
        <div className="form-input-box">
          <div>
            <div className="error-message">{errors.year}</div>
            <label className="form-label" htmlFor="title">
              Year:
            </label>
          </div>
          <div>
            <input
              id="title"
              type="number"
              onChange={(e) => setYear(e.target.value)}
              value={year}
            />
          </div>
        </div>
        <div>
          <div className="error-message">{errors.album_photo}</div>
          <label className="form-label" htmlFor="image">
            Upload an Album Cover:
          </label>
          <input
            id="image"
            type="file"
            name="image"
            accept="image/*"
            onChange={(e) => {
              setAlbum_Photo(e.target.files[0])
              if (e.target.files[0]) {
                const url = URL.createObjectURL(e.target.files[0])
                setImagePreview(url)
              } else {
                setImagePreview(null)
              }
            }}
          />
          {imagePreview && (
            <div>
              <img src={imagePreview} alt="album Image" width="100" />
            </div>
          )}
        </div>
        <div className="form-input-box">
          <div>
            <div className="error-message">{errors.date_created}</div>
            <label className="form-label" htmlFor="date_created">
              Date Created:
            </label>
          </div>
          <div>
            <input
              id="date_created"
              type="date"
              onChange={(e) => setDateCreated(e.target.value)}
              value={date_created}
            />
          </div>
        </div>
        <div>
          <button className="album-create-submit-button">Submit</button>
        </div>
      </form>
    </div>
  )
}

export default CreateAlbum
