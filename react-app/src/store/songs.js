const GET_SONG = '/songs/getSongs'
const GET_SINGLE_SONG = '/songs/getSingleSong'
const UPDATE_USER_SONG = '/songs/updateSong'
const DELETE_USER_SONG = '/songs/deleteSong'
const CREATE_NEW_SONG = '/songs/createSong'

// Song Action Creator
// const acCreateSong = (data) => {
//     return {
//         type: CREATE_NEW_SONG,
//         payload: data
//     }
// }

const acGetSongs = (data) => {
    return {
        type: GET_SONG,
        payload: data
    }
}

// const acGetSingleSong = (data) => {
//     return {
//         type: GET_SINGLE_SONG,
//         payload: data
//     }
// }

// const acUpdateSong = (data) => {
//     return {
//         type: UPDATE_USER_SONG,
//         payload: data
//     }
// }

// const acDeleteSong = (data) => {
//     return {
//         type: DELETE_USER_SONG,
//         payload: data
//     }
// }

// Song Thunk

export const getAllSongs = () => async (dispatch) => {
    try {
        const response = await fetch('/api/song/all');
        if (response.ok) {
            const data = await response.json();
            dispatch(acGetSongs(data));
            return data;
        } else {
            const errors = await response.json();
            return errors;
        }
    } catch (error) {
        console.error('An error occurred:', error);
        throw error; // Optionally, rethrow the error to propagate it further
    }
};

// Song Store

const initialState = { allSongs: {}, singleSong: {} }

const songReducer = (state = initialState, action) => {
    // let newState
    switch (action.type) {
        case GET_SONG: {
            return {
                ...state,
                allSongs: action.payload
            }
        }

        case CREATE_NEW_SONG:
            return {

            }
        case GET_SINGLE_SONG:
            return {

            }
        case UPDATE_USER_SONG:
            return {

            }
        case DELETE_USER_SONG:
            return {

            }
        default:
            return state
    }
}

export default songReducer