import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    post: {},
    currentPage: 1
}

const boardSlice = createSlice({
    name: "boardSlice",
    initialState,
    reducers: {
        setBoardPostSlice: (state, action) => {
            state.post = action.payload
        },
        setCurrentPageSlice: (state, action) => {
            state.currentPage = action.payload;
        }
    }
});

export const { setBoardPostSlice,setCurrentPageSlice } = boardSlice.actions

export default boardSlice.reducer