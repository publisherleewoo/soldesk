import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    post: {}
}

const boardSlice = createSlice({
    name: "boardSlice",
    initialState,
    reducers: {
        setPostSlice: (state, action) => {
            state.post = action.payload
        }
        
    }
});

export const { setPostSlice } = boardSlice.actions

export default boardSlice.reducer