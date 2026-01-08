import axios from "axios";
import React, { useRef } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

const BoardUpdate = () => {
   const titleInput = useRef();
   const contentTextArea = useRef();
  
   const navi = useNavigate();
   const post = useSelector((store) => store.bs.post);


   const updateBtn = () => {
      const fd = new FormData();
      fd.append("boardNo", post.no);
      fd.append("title", titleInput.current.value);
      fd.append("content", contentTextArea.current.value);

      axios
         .post("http://localhost:9999/board.update", fd)
         .then((res) => {
            alert(res.data.msg);
            navi("/b");
         })
         .catch((err) => {
            alert(err);
         });
   };

   const deleteBtn = () => {
      const fd = new FormData();
      fd.append("boardNo", post.no);

      axios
         .post("http://localhost:9999/board.delete", fd)
         .then((res) => {
            alert(res.data.msg);
            navi("/b");
         })
         .catch((err) => {
            alert(err);
         });
   };
   return (
      <div>
         <div id="detail_wrapper">
            <div className="detail_container">
               <header className="detail_header">
                  <span className="post_no">No. {post.no}</span>

                  <input
                     type="text"
                     className="detail_title_input"
                     ref={titleInput}
                     defaultValue={post.title}
                  />

                  <div className="post_info">
                     <span className="info_item">
                        <strong>작성자</strong> {post.writer}
                     </span>

                     <span className="info_item">
                        <strong>작성일</strong> {post.date}
                     </span>
                  </div>
               </header>

               <textarea
                  className="detail_content_input"
                  defaultValue={post.content}
                  ref={contentTextArea}
               ></textarea>

               <footer className="detail_buttons">
                  <button className="back_btn" onClick={() => navi(-1)}>
                     이전으로
                  </button>
                  <div className="edit_group">
                     <button className="edit_btn" onClick={updateBtn}>
                        수정
                     </button>
                     <button className="delete_btn" onClick={deleteBtn}>
                        삭제
                     </button>
                  </div>
               </footer>
            </div>
         </div>
      </div>
   );
};

export default BoardUpdate;
