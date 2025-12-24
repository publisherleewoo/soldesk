// state : 상태
// reducer : 기존state값 + 새로운값을 넣어주면, 새로운 state를 리턴하는 함수
// action : 액션
// slice : reducer + action

//rxslice  <- vscode 스니펫  
import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    fontSize: 30,  // 설정 1
}

const leeSizeSlice = createSlice({
    name: "abcd", //슬라이스 이름
    initialState,
    reducers: {
        //설정 2 함수:=>{값}
        sizeUp: (currentState, action) => {
            currentState.fontSize += 10;
        },
        sizeDown: (currentState, action) => {
            currentState.fontSize -= 10;
        }
    }
});

//설정 3 export{보낼 함수명1,보낼 함수명2}
export const { sizeUp, sizeDown } = leeSizeSlice.actions

export default leeSizeSlice.reducer
