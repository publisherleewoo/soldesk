import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import "./SecondDetailPage.css";
import axios from "axios";
import { useRef } from "react";

const SecondDetailPage = () => {
   const navi = useNavigate();
   const post = useSelector((store) => store.bs.post);
   const member = useSelector((store) => store.ms.loginMember);

   const titleInput = useRef();
   const contentTextArea = useRef();

   const user = post.writer === member.id;

   const updateBtn = () => {
      const fd = new FormData();
      fd.append("boardNo", post.no);
      fd.append("title", titleInput.current.value);
      fd.append("content", contentTextArea.current.value);
 
      axios
         .post("http://localhost:9999/board.update", fd)
         .then((res) => {
            alert(res.data.msg);
            navi('/b')
         })
         .catch((err) => {
            alert(err);
         });
   };

   const deleteBtn =()=>{
      const fd = new FormData();
      fd.append("boardNo", post.no);

      axios
         .post("http://localhost:9999/board.delete", fd)
         .then((res) => {
            alert(res.data.msg);
            navi('/b')
         })
         .catch((err) => {
            alert(err);
         });
   }

   return (
      <div id="detail_wrapper">
         <div className="detail_container">
            <header className="detail_header">
               <span className="post_no">No. {post.no}</span>
               {user ? (
                  <input
                     type="text"
                     className="detail_title_input"
                     ref={titleInput}
                     defaultValue={post.title}
                  />
               ) : (
                  <h1 className="detail_title">{post.title}</h1>
               )}

               <div className="post_info">
                  <span className="info_item">
                     <strong>작성자</strong> {post.writer}
                  </span>
                  {user ? null : (
                     <span className="info_item">
                        <strong>작성일</strong> {post.date}
                     </span>
                  )}
               </div>
            </header>

            {user ? (
               <textarea
                  className="detail_content_input"
                  defaultValue={post.content}
                  ref={contentTextArea}
               ></textarea>
            ) : (
               <section className="detail_content">{post.content}</section>
            )}

            <footer className="detail_buttons">
               <button className="back_btn" onClick={() => navi(-1)}>
                  목록으로
               </button>
               {user && (
                  <div className="edit_group">
                     <button className="edit_btn" onClick={updateBtn}>
                        수정완료
                     </button>
                     <button className="delete_btn" onClick={deleteBtn}>삭제</button>
                  </div>
               )}
            </footer>
         </div>
      </div>
   );
};

export default SecondDetailPage;
