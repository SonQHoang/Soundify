const GET_PLAYLISTS = '/playlists/getPlaylist'
const GET_USER_PLAYLIST = '/playlists/getUserPlaylist'
const GET_SINGLE_PLAYLIST = '/playlists/getSinglePlaylist'
const UPDATE_USER_PLAYLIST = '/playlists/updatePlaylist'
const DELETE_USER_PLAYLIST = '/playlists/deletePlaylist'
const CREATE_NEW_PLAYLIST = '/playlists/createPlaylist'
const ADD_SONG_TO_PLAYLIST = '/playlists/addSongToPlaylist'
const GET_PLAYLIST_SONGS = '/playlists/getPlaylistSongs'

const acGetPlaylistSongs = (data) => {
    // console.log('Is this the data that I want============>', data)
    return {
        type: GET_PLAYLIST_SONGS,
        payload: data
    }
}

const acGetUserPlaylist = (data) => {
    return {
        type: GET_USER_PLAYLIST,
        payload: data
    }
}

const acUpdatePlaylist = (data) => {
    // console.log('Is the acUpdate still going through======>', data)
    return {
        type: UPDATE_USER_PLAYLIST,
        payload: data
    }
}

const acDeletePlaylist = (data) => {
    return {
        type: DELETE_USER_PLAYLIST,
        payload: data
    }
}

const acAddSongToPlaylist = (data) => {
    // console.log('What is the song I am adding======>', data)
    return {
        type: ADD_SONG_TO_PLAYLIST,
        payload: data
    }
}
const acCreatePlaylist = (data) => {
    console.log('is my image reaching my action creator=========>', data)
    return {
        type: CREATE_NEW_PLAYLIST,
        payload: data
    }
}

const acGetPlaylist = (data) => {
    return {
        type: GET_PLAYLISTS,
        payload: data
    }
}

const acGetSinglePlaylist = (data) => {
    return {
        type: GET_SINGLE_PLAYLIST,
        payload: data
    }
}

export const getUserPlaylist = () => async (dispatch) => {
    const response = await fetch(`/api/playlist/user_playlist`)
    if (response.ok) {
        const playlist = await response.json()
        // console.log('playlist=======>', playlist)
        dispatch(acGetUserPlaylist(playlist))
    }
}

export const UpdatePlaylistThunk = (playlistId, updatedData) => async (dispatch) => {
    // console.log('Is the playlistId coming through for the THUNK======>', playlistId)
    // console.log('Is the updatedDat coming through======>', updatedData)
    try {
        const response = await fetch(`/api/playlist/update/${playlistId}`, {
            method: "PUT",
            headers: { "Content-Type": 'application/json' },
            body: JSON.stringify(updatedData)
        });
        // console.log('What does the response look like for the thunk after the backend=========>', response)
        if (response.ok) {
            dispatch(acUpdatePlaylist(playlistId))
        }
    } catch (error) {
        console.error(error)
    }
}

export const DeletePlaylistThunk = (playlistId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/playlist/delete/${playlistId}`, {
            method: "DELETE",
            headers: { "Content-Type": 'application/json' }
        });
        if (response.ok) {
            dispatch(acDeletePlaylist(playlistId))
        }
    } catch (error) {
        console.error(error)
    }
}

export const GetSongsForPlaylist = (playlistId) => async (dispatch) => {
    console.log('playlistId thunk===================>', playlistId) 
    const response = await fetch(`/api/playlist/${playlistId}/songs`, {
    })
    if (response.ok) {
        const playlist_songs = await response.json()
        console.log('playlist_songs for Taylor Swift====>', playlist_songs)
        dispatch(acGetPlaylistSongs(playlist_songs))
        return playlist_songs
    } else {
        console.error(`Request failed with status ${response.status}`);
    }
}


export const AddSongToPlaylist = (data) => async (dispatch) => {
    const { playlistId } = data
    const intPlaylistId = parseInt(playlistId, 10)
    // console.log('playlistId, songId ============>', intPlaylistId)
    // console.log("********* in AddSongToPlaylist, data:", data.id)
    // console.log('What is the data here when I add a song to a playlist THUNK====>', data)
    const response = await fetch(`/api/playlist/${intPlaylistId}/add`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    // console.log('**************AddSongToPlaylist response', response)
    if (response.ok) {
        const data = await response.json()
        // console.log('**************AddSongToPlaylist res.ok data', data)
        dispatch(acAddSongToPlaylist(data))
        // console.log('In AddSongToPlaylist=============>', data)
        return data
    } else {
        console.log("Could not add song to your playlist")
    }
}

export const GetSinglePlaylist = (playlistId) => async (dispatch) => {
    const response = await fetch(`/api/playlist/${playlistId}`)
    // console.log('What does the respone for a singlePlaylist look like======>', response)
    if (response.ok) {
        const playlist = await response.json()
        dispatch(acGetSinglePlaylist(playlist))
    } else {
        console.log("Could not retrieve the specified playlist")
    }
}

export const createPlaylist = (data) => async (dispatch) => {
    console.log('What data is coming through?=======> FormData', data)
    // for (const [key, value] of data.entries()) {
    //     console.log(`Key: ${key}, Value: ${value}`);
    // }
    const response = await fetch('/api/playlist/new', {
        method: "POST",
        body: data
    })
    console.log('What is my response looking like=======>', response)
    if (response.ok) {
        const new_playlist = await response.json()
        dispatch(acCreatePlaylist(new_playlist))
        console.log("NEW PLAYLIST DATA =======>", new_playlist)
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

// let newState
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
                allPlaylists: action.payload,
            }
        }
        case CREATE_NEW_PLAYLIST:
            // console.log('action=======>', action.payload.id)
            return {
                ...state,
                allPlaylists: {
                    ...state.allPlaylists,
                    [action.payload.resPost.id]: action.payload,
                },
                singlePlaylist: action.payload.resPost
            };
        case ADD_SONG_TO_PLAYLIST: {
            const updatedState = {
                ...state,
                singlePlaylist: {
                    ...state.singlePlaylist,
                    songs: [...(state.singlePlaylist.songs || []), action.payload],
                },
            };
            return updatedState;
        }

        case GET_SINGLE_PLAYLIST:
            return {
                ...state,
                singlePlaylist: action.payload
            }

        case UPDATE_USER_PLAYLIST:
            return {
                ...state,
                allPlaylists: {
                    ...state.allPlaylists,
                    [action.payload.id]: action.payload,
                },
            }

        case DELETE_USER_PLAYLIST: {
                const newState = { ...state, allPlaylists: { ...state.allPlaylists } }
                delete newState.allPlaylists[action.payload]
                return newState
            }

        case GET_PLAYLIST_SONGS: {
            return {
                ...state,
                singlePlaylist: {
                    ...state.singlePlaylist,
                    songs: [action.payload.id] = action.payload,
                }
            }
        }
        default:
            return state
    }
}

export default playlistReducer