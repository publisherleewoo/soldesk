import  { useRef } from "react";

const ReplyArea = ({ addReply }) => {
   const replyTextarea = useRef();

   const btnFunc = () => {
      addReply(replyTextarea.current.value);

   };

   return (
      <div className="comment_form">
         <textarea
            placeholder="댓글을 입력하세요..."
            className="comment_input"
            ref={replyTextarea}
         ></textarea>
         <button className="comment_submit_btn" onClick={btnFunc}>
            등록
         </button>
      </div>
   );
};

export default ReplyArea;
