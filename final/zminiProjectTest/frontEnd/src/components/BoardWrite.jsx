import { useEffect, useRef } from "react";
import { useTokenCheck } from "../../lib/useTokenCheck";
import "./BoardWrite.css";
import axios from "axios";
import { useSelector } from "react-redux";

const BoardWrite = ({ setBoardView }) => {
   const check = useTokenCheck();
   const writeInput = useRef();
   const writeTextarea = useRef();
   const loginMember = useSelector(store =>store.ms.loginMember)

   useEffect(() => {
      check();
      
   }, []);

   const createBoardWrite = () => {
      const fd = new FormData();
      fd.append("id", loginMember.id);
      fd.append("title", writeInput.current.value);
      fd.append("content", writeTextarea.current.value);
      axios
         .post("http://localhost:9999/board.post", fd)
         .then((res) => {
            if(res.data.msg === "등록완료"){
               alert('등록되었습니다')
               setBoardView(false)
            }else{
               alert("등록실패했습니다")
            }
         })
         .catch((err) => alert(err));
   };

   return (
      <div className="board_write_container">
         <h2 className="write_title">게시글 작성</h2>

         <div className="input_group">
            <label>제목</label>
            <input
               type="text"
               ref={writeInput}
               placeholder="제목을 입력하세요"
               className="write_input"
            />
         </div>

         <div className="input_group">
            <label>내용</label>
            <textarea
               ref={writeTextarea}
               placeholder="내용을 입력하세요"
               className="write_textarea"
            ></textarea>
         </div>

         <div className="write_button_area">
            <button className="cancel_btn" onClick={() => setBoardView(false)}>
               취소
            </button>
            <button className="submit_btn" onClick={createBoardWrite}>
               등록
            </button>
         </div>
      </div>
   );
};

export default BoardWrite;
