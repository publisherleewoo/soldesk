import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    post: {}
}

const boardSlice = createSlice({
    name: "boardSlice",
    initialState,
    reducers: {
        setBoardPostSlice: (state, action) => {
            state.post = action.payload
        }
        
    }
});

export const { setBoardPostSlice } = boardSlice.actions

export default boardSlice.reducer