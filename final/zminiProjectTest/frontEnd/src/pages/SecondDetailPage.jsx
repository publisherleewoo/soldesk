import { useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import CommentList from "../components/CommentList";
import "./SecondDetailPage.css";
import ReplyArea from "../components/ReplyArea";
import axios from "axios";
import { useEffect, useState } from "react";

const SecondDetailPage = () => {
   const navi = useNavigate();
   const post = useSelector((store) => store.bs.post);
   const params = useParams();
   const member = useSelector((store) => store.ms.loginMember);
   const user = post.writer === member.id;
   const [replys, setReplys] = useState([])


   const updateBtn = () => {
      navi(`/b/${params.no}/update`);
   };

   const addReply = (replyTextareaValue) => {
      const fd = new FormData();
      fd.append("boardNo", post.no);
      fd.append("id", member.id);
      fd.append("reply", replyTextareaValue);
      axios
         .post("http://localhost:9999/board.reply.post", fd)
         .then((res) => {
            if(res.data.msg==="댓글등록성공"){
               getReply()
            }
         })
         .catch((err) => alert(err));
   };

   const getReply = ()=>{
      if(!post.no){
         navi('/b')
      }
      axios
         .get(`http://localhost:9999/board.reply.get?postNo=${post.no}`)
         .then((res) => {
            console.log(res);
            if(res.data.msg==="조회성공"){
               setReplys(res.data.replys)
            } 
         })
         .catch((err) => alert(err));
   }
   useEffect(() => {
      
     getReply()

   }, []);

   return (
      <div id="detail_wrapper">
         <div className="detail_container">
            <header className="detail_header">
               <span className="post_no">No. {post.no}</span>

               <h1 className="detail_title">{post.title}</h1>

               <div className="post_info">
                  <span className="info_item">
                     <strong>작성자</strong> {post.writer}
                  </span>

                  <span className="info_item">
                     <strong>작성일</strong> {post.date}
                  </span>
               </div>
            </header>

            <section className="detail_content">{post.content}</section>

            <footer className="detail_buttons">
               <button className="back_btn" onClick={() => navi(-1)}>
                  목록으로
               </button>

               {user && (
                  <div className="edit_group">
                     <button className="edit_btn" onClick={updateBtn}>
                        수정
                     </button>
                  </div>
               )}
            </footer>

            <hr className="divider" />
            <section className="comment_section">
               <h3>댓글</h3>

               {replys.map((r,i)=><CommentList
                  key ={i}
                  replyNo={r.no}
                  replyId={r.writer}
                  replyDate={r.date}
                  replyContnet={r.content}
                  getReply={getReply}
               />
               )}

               <ReplyArea addReply={addReply} />
            </section>
         </div>
      </div>
   );
};

export default SecondDetailPage;
