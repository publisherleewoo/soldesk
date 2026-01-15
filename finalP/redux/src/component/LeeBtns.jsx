import { useDispatch } from "react-redux";
import { sizeDown, sizeUp } from "../leeSizeSlice";

//dispatcher : state를 바꿀 존재
const LeeBtns = () => {
   //설정6. dispatcher 셋팅
   const d = useDispatch();

   return (
      <div>
         <button
            onClick={() => {
               // 설정7 dispatcher와 실행할 함수명 실행하기
               d(sizeUp());
            }}
         >
            크게
         </button>
         <button
            onClick={() => {
               // 설정7 dispatcher와 실행할 함수명 실행하기
               d(sizeDown());
            }}
         >
            작게
         </button>
      </div>
   );
};

export default LeeBtns;
