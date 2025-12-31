import { createSlice } from "@reduxjs/toolkit";

const initialState = {
   loginMember: {},
};

const memberSlice = createSlice({
   name: "ms",
   initialState,
   reducers: {
      setLoginMember: (state, action) => {
         state.loginMember = action.payload;
      },
   },
});

export const { setLoginMember } = memberSlice.actions;

export default memberSlice.reducer;
