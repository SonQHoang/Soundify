const GET_SONG = '/songs/getSongs'
const GET_SINGLE_SONG = '/songs/getSingleSong'
const UPDATE_USER_SONG = '/songs/updateSong'
const DELETE_USER_SONG = '/songs/deleteSong'
const CREATE_NEW_SONG = '/songs/createSong'

// Song Action Creator
const createSong = (data) => {
    return {
        type: CREATE_NEW_SONG,
        payload: data
    }
}

const getSongs = (data) => {
    return {
        type: GET_SONG,
        payload: data
    }
}

const getSingleSong = (data) => {
    return {
        type: GET_SINGLE_SONG,
        payload: data
    }
}

const updateSong = (data) => {
    return {
        type: UPDATE_USER_SONG,
        payload: data
    }
}

const deleteSong = (data) => {
    return {
        type: DELETE_USER_SONG,
        payload: data
    }
}

// Song Thunk

export const getAllSongs = () => async (dispatch) => {
    try {
        const response = await fetch('/api/songs/all')
        if (response.ok) {
            const data = await response.json();
            dispatch(getSongs(data))
            return data
        } else {
            const errors = await response.json();
            return errors
        }
    } catch (error) {
        const errors = (error && error.json) ? await error.json() : { message: error.toString() }
        return errors;
    }
}

// Song Store

const initialState = { allSongs: {}, singleSong: {} }

const songReducer = (state = initialState, action) => {
    let newState
    switch (action.type) {
        case GET_SONG:

        case CREATE_NEW_SONG:

        case GET_SINGLE_SONG:

        case UPDATE_USER_SONG:

        case DELETE_USER_SONG:

        default:
            return state
    }
}

export default songReducer