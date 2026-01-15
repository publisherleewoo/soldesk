import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";

const CommentList = ({
   replyNo,
   replyId,
   replyDate,
   replyContnet,
   getReply,
}) => {
   const member = useSelector((store) => store.ms.loginMember);
   const [edit, setEdit] = useState(false);
   const ta = useRef();

   const editFunc = () => {
      setEdit(!edit);
   };

   useEffect(() => {
      if (ta.current) {
         ta.current.value = replyContnet;
      }
   }, [edit, replyContnet]);

   const updateReply = () => {
      const fd = new FormData();
      fd.append("replyNo", replyNo);
      fd.append("reply", ta.current.value);
      axios
         .post("http://localhost:9999/board.reply.update", fd)
         .then((res) => {
            alert(res.data.msg);
            setEdit(!edit);
            getReply();
         })
         .catch((err) => alert(err));
   };

   const deleteFunc = () => {
      const fd = new FormData();
      fd.append("replyNo", replyNo);
      axios
         .post("http://localhost:9999/board.reply.delete", fd)
         .then((res) => {
            alert(res.data.msg);
            getReply();
         })
         .catch((err) => alert(err));
   };

   return (
      <div id="comment_list">
         <div className="comment_item">
            <div className="comment_meta">
               <div className="comment_info_row">
                  <span className="comment_author">{replyId}</span>
                  <span className="comment_date">{replyDate}</span>
               </div>

               {member.id === replyId && !edit && (
                  <div className="comment_actions">
                     <button className="comment_edit_btn" onClick={editFunc}>
                        수정
                     </button>
                     <button
                        className="comment_delete_btn"
                        onClick={deleteFunc}
                     >
                        삭제
                     </button>
                  </div>
               )}
            </div>
            {edit ? (
               <>
                  <input className="comment_input" ref={ta} />
                  <button className="comment_submit_btn" onClick={updateReply}>
                     수정
                  </button>
                  &nbsp;&nbsp;
                  <button
                     className="comment_submit_btn"
                     style={{ background: "gray" }}
                     onClick={() => {
                        setEdit(!edit);
                     }}
                  >
                     취소
                  </button>
               </>
            ) : (
               <p className="comment_text">{replyContnet}</p>
            )}
         </div>
      </div>
   );
};

export default CommentList;
