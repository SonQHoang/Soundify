const GET_PLAYLISTS = '/playlists/getPlaylist'
const GET_USER_PLAYLIST = '/playlists/getUserPlaylist'
const GET_SINGLE_PLAYLIST = '/playlists/getSinglePlaylist'
const UPDATE_USER_PLAYLIST = '/playlists/updatePlaylist'
const DELETE_USER_PLAYLIST = '/playlists/deletePlaylist'
const CREATE_NEW_PLAYLIST = '/playlists/createPlaylist'
const ADD_SONG_TO_PLAYLIST = '/playlists/addSongToPlaylist'

const acGetUserPlaylist = (data) => {
    // console.log('data from acUserPlaylist=======>', data)
    return {
        type: GET_USER_PLAYLIST,
        payload: data
    }
}
const acDeletePlaylist = (data) => {
    console.log('What is this data from acDeletePlaylist=====>', data)
    return {
        type: DELETE_USER_PLAYLIST,
        payload: data
    }
}
const acAddSongToPlaylist = (data) => {
    // console.log('Testing the data coming from acAddToPlaylist=====>', data)
    return {
        type: ADD_SONG_TO_PLAYLIST,
        payload: data
    }
}
const acCreatePlaylist = (data) => {
    // console.log('data========>', data.id)
    return {
        type: CREATE_NEW_PLAYLIST,
        payload: data
    }
}

const acGetPlaylist = (data) => {
    // console.log('acGetPlaylist data===========>', data)
    return {
        type: GET_PLAYLISTS,
        payload: data
    }
}

const acGetSinglePlaylist = (data) => {
    // console.log('acSinglePlaylist data ========>',data)
    return {
        type: GET_SINGLE_PLAYLIST,
        payload: data
    }
}

export const getUserPlaylist = () => async (dispatch) => {
    const response = await fetch(`/api/playlist/user_playlist`)
    // console.log('Do I get a 200 response=======+> Yes', response)
    if(response.ok) {
        const playlist = await response.json()
        console.log('playlist=======>', playlist)
        dispatch(acGetUserPlaylist(playlist))
    }
}

export const DeletePlaylistThunk = (playlistId) => async (dispatch) => {
    console.log('Is the playlistId going through======>', playlistId)
    try {
        const response = await fetch(`/api/playlist/delete/${playlistId}`, {
            method: "DELETE",
            headers: {"Content-Type": 'application/json'}
        });
        console.log('What does my response look like======>', response)
        if (response.ok) {
            dispatch(acDeletePlaylist(playlistId))
        }
    } catch (error) {
        console.error(error)
    }
}


export const AddSongToPlaylist = (data) => async (dispatch) => {
    console.log("What is the data that is coming from AddSongToPlaylist Thunk=======+>", data)
    const response = await fetch('/api/playlist/add', {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    console.log('What is my response when adding a song to the playlist====>', response)
    if (response.ok) {
        const data = await response.json()
        // console.log('What does the data from the backend of adding a playlist look like====>', data)
        dispatch(acAddSongToPlaylist(data))
        return data
    } else {
        console.log("Could not add song to your playlist")
    }
}

export const GetSinglePlaylist = (playlistId) => async (dispatch) => {
    // console.log('playlistId=======>', playlistId)
    const response = await fetch(`/api/playlist/${playlistId}`)
    // console.log('What does the respone for a singlePlaylist look like======>', response)
    if (response.ok) {
        const playlist = await response.json()
        // console.log('what does the playlist data look like======>', playlist)
        dispatch(acGetSinglePlaylist(playlist))
    } else {
        console.log("Could not retrieve the specified playlist")
    }
}


export const createPlaylist = (data) => async (dispatch) => {
    // console.log('What data is coming through?=======> FormData', data)
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

export const getAllPlaylists = () => async (dispatch) => {
    const response = await fetch('/api/playlist/all')
    console.log('response========>', response)
    if (response.ok) {
        const data = await response.json()
        dispatch(acGetPlaylist(data))
        return data
    } else {
        console.log('There was an error loading all of your playlists')
    }
}

// Playlist Store

const initialState = { allPlaylists: {}, singlePlaylist: {} }

let newState
const playlistReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_PLAYLISTS: {
            return {
                ...state,
                allPlaylists: action.payload
            }
        }
        case GET_USER_PLAYLIST: {
            // console.log('my get user playlist action=====>', action)
            return {
                ...state,
                allPlaylists: action.payload
            }
        }
        case CREATE_NEW_PLAYLIST:
            // console.log('action=======>', action.payload.id)
            return {
                ...state,
                allPlaylists: {
                    ...state.allPlaylists,
                    [action.payload.id]: action.payload,
                },
            };
        case ADD_SONG_TO_PLAYLIST:
            // console.log('My intial state=====>', state)
            // console.log('My song action payload=====>', action.payload)
            return {
                ...state,
                singlePlaylist: {
                    ...state.singlePlaylist,
                    [action.payload.id]: action.payload
                }
            }
        case GET_SINGLE_PLAYLIST:
            return {
                ...state,
                singlePlaylist: action.payload
            }
            
        case UPDATE_USER_PLAYLIST:

        case DELETE_USER_PLAYLIST: {
            const newState = { ...state, allPlaylists: { ...state.allPlaylists } }
            delete newState.allPlaylists[action.tipId]
            return newState
        }
        default:
            return state
    }
}

export default playlistReducer