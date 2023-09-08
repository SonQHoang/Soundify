const GET_PLAYLISTS = '/playlists/getPlaylist'
const GET_SINGLE_PLAYLIST = '/playlists/getSinglePlaylist'
const UPDATE_USER_PLAYLIST = '/playlists/updatePlaylist'
const DELETE_USER_PLAYLIST = '/playlists/deletePlaylist'
const CREATE_NEW_PLAYLIST = '/playlists/createPlaylist' 

const acCreatePlaylist = (data) => {
    // console.log('data========>', data.id)
    return {
        type: CREATE_NEW_PLAYLIST,
        payload: data
    }
}

export const createPlaylist = (data) => async (dispatch) => {
    console.log('What data is coming through?=======> FormData', data)
        const response = await fetch('/api/playlist/new', {
            method: "POST",
            body: data
        })
        console.log('What is my response looking like=======>', response)
        if (response.ok) {
            const { resPost } = await response.json()
            console.log("NEW PLAYLIST DATA =======>", resPost)
            dispatch(acCreatePlaylist(resPost)) 
        } else {
            console.log("There was an error creating your playlist!")
        }
}

// Playlist Store

const initialState = { allPlaylists: {}, singlePlaylist: {} }

let newState
const playlistReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_PLAYLISTS:

        case CREATE_NEW_PLAYLIST:
            // console.log('action=======>', action.payload.id)
            return {
                ...state,
                allPlaylists: {
                    ...state.allPlaylists,
                    [action.payload.id]: action.payload, 
                },
            };
        case GET_SINGLE_PLAYLIST:

        case UPDATE_USER_PLAYLIST:

        case DELETE_USER_PLAYLIST:

        default:
            return state
    }
}

export default playlistReducer