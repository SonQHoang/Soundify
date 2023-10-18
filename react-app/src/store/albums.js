const GET_ALBUMS = '/albums/getAlbum'
const GET_USER_ALBUM = '/albums/getUserAlbum'
const GET_SINGLE_ALBUM = '/albums/getSingleAlbum'
const UPDATE_USER_ALBUM = '/albums/updateAlbum'
const DELETE_USER_ALBUM = '/albums/deleteAlbum'
const CREATE_NEW_ALBUM = '/albums/createAlbum'
const ADD_SONG_TO_ALBUM = '/albums/addSongToAlbum'
const GET_ALBUM_SONGS = '/albums/getAlbumSongs'

const acGetAlbumSongs = (data) => {
    return {
        type: GET_ALBUM_SONGS,
        payload: data
    }
}

const acGetUserAlbum = (data) => {
    return {
        type: GET_USER_ALBUM,
        payload: data
    }
}

const acUpdateAlbum = (data) => {
    return {
        type: UPDATE_USER_ALBUM,
        payload: data
    }
}

const acDeleteAlbum = (data) => {
    return {
        type: DELETE_USER_ALBUM,
        payload: data
    }
}
const acAddSongToAlbum = (data) => {
    return {
        type: ADD_SONG_TO_ALBUM,
        payload: data
    }
}
const acCreateAlbum = (data) => {
    return {
        type: CREATE_NEW_ALBUM,
        payload: data
    }
}

const acGetAllAlbum = (data) => {
    return {
        type: GET_ALBUMS,
        payload: data
    }
}

const acGetSingleAlbum = (data) => {
    return {
        type: GET_SINGLE_ALBUM,
        payload: data
    }
}

export const getUserAlbum = () => async (dispatch) => {
    const response = await fetch(`/api/album/user_album`)
    if (response.ok) {
        const album = await response.json()
        dispatch(acGetUserAlbum(album))
    }
}

export const updateAlbumThunk = (albumId, formData) => async (dispatch) => {
    const formDataObject = {};
    formData.forEach((value, key) => {
            formDataObject[key] = value;
        });
    try {
        const response = await fetch(`/api/album/update/${albumId}`, {
            method: 'PUT',
            body: formData
        });
        
        if (response.ok) {
            const updatedData = await response.json()
            dispatch(acUpdateAlbum(updatedData))
            return updatedData
        }
    } catch (error) {
        console.error(error)
    }
}

export const deleteAlbumThunk = (albumId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/album/delete/${albumId}`, {
            method: "DELETE",
            headers: { "Content-Type": 'application/json' }
        });
        if (response.ok) {
            dispatch(acDeleteAlbum(albumId))
        }
    } catch (error) {
        console.error(error)
    }
}

export const GetSongsForAlbum = (albumId) => async (dispatch) => {
    const response = await fetch(`/api/album/${albumId}/songs`, {
    })
    if (response.ok) {
        const album_songs = await response.json()
        dispatch(acGetAlbumSongs(album_songs))
        return album_songs
    } else {
        console.error(`Request failed with status ${response.status}`);
    }
}

export const AddSongToAlbum = (data) => async (dispatch) => {
    const { albumId } = data
    const intAlbumId = parseInt(albumId, 10)

    const response = await fetch(`/api/album/${intAlbumId}/add`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(acAddSongToAlbum(data))
        return data 
    } else {
        console.log("Could not add song to your album")
    }
}

export const GetSingleAlbum = (albumId) => async (dispatch) => {
    const response = await fetch(`/api/album/${albumId}`)
    if (response.ok) {
        const album = await response.json()
        dispatch(acGetSingleAlbum(album))
    } else {
        console.log("Could not retrieve the specified album")
    }
}

export const createAlbum = (data) => async (dispatch) => {
    const response = await fetch('/api/album/new', {
        method: "POST", 
        body: data
    })
    console.log('What is my response coming back from the backend=====>', response)
    if (response.ok) {
        const new_album = await response.json()
        dispatch(acCreateAlbum(new_album))
    } else {
        console.log("There was an error creating your album!")
    }
}

export const getAllAlbums = () => async (dispatch) => {
    const response = await fetch('/api/album/all')
    if (response.ok) {
        const data = await response.json()
        dispatch(acGetAllAlbum(data))
        return data
    } else {
        console.log('There was an error loading all of your albums')
    }
}

// Album Store

const initialState = { allAlbums: {}, singleAlbum: {} }

// let newState
const albumReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALBUMS: {
            return {
                ...state,
                allAlbums: action.payload
            }
        }
        case GET_USER_ALBUM: {
            return {
                ...state,
                allAlbums: action.payload
            }
        }
        case CREATE_NEW_ALBUM:
            return {
                ...state,
                allAlbums: {
                    ...state.allAlbums,
                    [action.payload.id]: action.payload,
                },
                singleAlbum: action.payload.resPost
            };
        case ADD_SONG_TO_ALBUM:
            const updatedState = {
                ...state,
                singleAlbum: {
                    ...state.singleAlbum,
                    songs: [...(state.singleAlbum.songs || []), action.payload],
                },
            };

            return updatedState;

        case GET_SINGLE_ALBUM:
            return {
                ...state,
                singleAlbum: action.payload
            }

        case UPDATE_USER_ALBUM:
            return {
                ...state,
                allAlbums: {
                    ...state.allAlbums,
                    [action.payload.id]: action.payload
                }
            }

        case DELETE_USER_ALBUM: {
            const newState = { ...state, allAlbums: { ...state.allAlbums } }
            delete newState.allAlbums[action.tipId]
            return newState
        }

        case GET_ALBUM_SONGS: {
            return {
                ...state,
                singleAlbum: {
                    ...state.singleAlbum,
                    songs: [action.payload.id] = action.payload,
                }
            }
        }
        default:
            return state
    }
}

export default albumReducer