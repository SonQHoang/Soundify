const GET_ALBUMS = '/albums/getAlbum'
const GET_USER_ALBUM = '/albums/getUserAlbum'
const GET_SINGLE_ALBUM = '/albums/getSingleAlbum'
const UPDATE_USER_ALBUM = '/albums/updateAlbum'
const DELETE_USER_ALBUM = '/albums/deleteAlbum'
const CREATE_NEW_ALBUM = '/albums/createAlbum'
const ADD_SONG_TO_ALBUM = '/albums/addSongToAlbum'

const acGetUserAlbum = (data) => {
    return {
        type: GET_USER_ALBUM,
        payload: data
    }
}

const acUpdateAlbum = (data) => {
    console.log('Is the acUpdate still going through======>', data)
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
    console.log('Is my new album data coming through=====>', data)
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
    console.log('What does my response look like for getting the userAlbum====>', response)
    if (response.ok) {
        const album = await response.json()
        console.log('album=======>', album)
        dispatch(acGetUserAlbum(album))
    }
}

export const updateAlbumThunk = (albumId, updatedData) => async (dispatch) => {
    console.log('Is the albumId coming through for the THUNK======>', albumId)
    console.log('Is the updatedDat coming through======>', updatedData)
    try {
        const response = await fetch(`/api/album/update/${albumId}`, {
            method: "PUT",
            headers: { "Content-Type": 'application/json' },
            body: JSON.stringify(updatedData)
        });
        console.log('What does the response look like for the thunk after the backend=========>', response)
        if (response.ok) {
            const updatedData = await response.json()
            console.log('What does the updatedData look like, updateAlbumThunk**************', updatedData)
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


export const AddSongToAlbum = (data) => async (dispatch) => {
    // console.log('What is the data here when I add a song to a album THUNK====>', data)
    const response = await fetch('/api/album/add', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    // console.log('What does the response from the backend look like=====>', response)
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
    // console.log('What does the respone for a singleAlbum look like======>', response)
    if (response.ok) {
        const album = await response.json()
        dispatch(acGetSingleAlbum(album))
    } else {
        console.log("Could not retrieve the specified album")
    }
}

export const createAlbum = (data) => async (dispatch) => {
    console.log('What data is coming through?=======> FormData', data)
    for (const [key, value] of data.entries()) {
        console.log(`Key: ${key}, Value: ${value}`);
    }

    const response = await fetch('/api/album/new', {
        method: "POST",
        body: data
    })
    console.log('What is my response looking like=======>', response)
    if (response.ok) {
        const { resPost } = await response.json()
        console.log("NEW ALBUM DATA =======>", resPost)
        dispatch(acCreateAlbum(resPost))
    } else {
        console.log("There was an error creating your album!")
    }
}

export const getAllAlbums = () => async (dispatch) => {
    const response = await fetch('/api/album/all')
    console.log('response========>', response)
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

let newState
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
            };
        case ADD_SONG_TO_ALBUM:
            console.log('My initial state =====>', state);
            console.log('My song action payload =====>', action.payload);

            const updatedState = {
                ...state,
                singleAlbum: {
                    ...state.singleAlbum,
                    [action.payload.id]: action.payload
                }
            };

            console.log('Updated state =====>', updatedState);

            return updatedState;

        case GET_SINGLE_ALBUM:
            return {
                ...state,
                singleAlbum: action.payload
            }

        case UPDATE_USER_ALBUM:
            return {
                ...state,
                singleAlbum: {
                    ...state.singleAlbum,
                    [action.payload.id]: action.payload
                }
            }

        case DELETE_USER_ALBUM: {
            const newState = { ...state, allAlbums: { ...state.allAlbums } }
            delete newState.allAlbums[action.tipId]
            return newState
        }
        default:
            return state
    }
}

export default albumReducer