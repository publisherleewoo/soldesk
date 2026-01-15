import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    loginMember: {}  //state값  
}

const memberSlice = createSlice({
    name: "memberSlice",
    initialState,
    reducers: {
        setLoginMember: (state, action) => {   //setState하는 메서드
            state.loginMember = action.payload          
        }
        
    }
});

export const { setLoginMember } = memberSlice.actions

export default memberSlice.reducer