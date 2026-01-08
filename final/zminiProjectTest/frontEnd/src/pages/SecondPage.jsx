import axios from "axios";
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { useTokenCheck } from "../../lib/useTokenCheck";
import BoardWrite from "../components/BoardWrite";
import { setBoardPostSlice } from "../store/boardSlice";
import "./SecondPage.css";
import SearchInput from "../components/SearchInput";

const SecondPage = () => {
   const [posts, setPosts] = useState("");
   const [allPage, setAllPage] = useState(0);
   const view = 5;
   const [count, setCount] = useState(1);
   const [selectPage, setSelectPage] = useState(1);
   const checkToken = useTokenCheck();
   const navi = useNavigate();
   const [boardView, setBoardView] = useState(false);
   const d = useDispatch();

   useEffect(() => {
      axios
         .get("http://localhost:9999/board.get?nowPageNo=1")
         .then((res) => {
            if (res.data.msg === "성공") {
               setPosts(res.data.boards);
               setAllPage(res.data.allPage);
            }
         })
         .catch((err) => alert(err));
   }, [d, boardView,allPage]);

   const createBoard = () => {
      const memberId = sessionStorage.getItem("loginMember");
      if (memberId) {
         checkToken(memberId);
      } else {
         alert("로그인해주세요");
         navi("/login");
      }
      setBoardView(true);
   };

   const gotoBoardDetail = (post) => {
      navi(`/b/${post.no}`);
      d(setBoardPostSlice(post));
   };

   // const inpRequestBoard = (str)=>{
   //    axios.get(`http://localhost:9999/board.input.get?str=${str}`).then(res=>{
   //       setPosts(res.data.boards)
   //       // setAllPage(res.data.allPage)
   //       // setSelectPage(1)
   //       // setCount(1)
   //       console.log(res.data.boards,res.data.allPage);
   //    }
   
   
   // ).catch(err=>alert(err))
   // }



   const requestBoard = (i) => {

      axios
         .get(`http://localhost:9999/board.get?nowPageNo=${i}`)
         .then((res) => {
            if (res.data.msg === "성공") {
               setPosts(res.data.boards);
            }
         })
         .catch((err) => alert(err));
   };

   const pageList = () => {
      const listItem = [];

      for (let i = view * (count - 1) + 1; i <= view * count; i++) {
         if (i > allPage) break;
         let newlist = (
            <li key={i}>
               <a
                  href="#"
                  className={selectPage == i ? "active" : null}
                  onClick={(e) => {
                     e.preventDefault();
                     requestBoard(i);
                     setSelectPage(i);
                  }}
               >
                  {i}
               </a>
            </li>
         );
         listItem.push(newlist);
      }

      return listItem;
   };

   return (
      <div id="SecondPage">
         {/* <aside className="side_bar">
            <div className="side_title">COMMUNITY</div>
            <ul>
               <li className="active">자유게시판</li>
               <li>공지사항</li>
               <li>자료실</li>
               <li>문의하기</li>
            </ul>
         </aside> */}

         <section className="main_board">
            <div className="board_header_text">
               <h3>자유게시판</h3>
            </div>

            <div className="board_top">
               {/* <SearchInput inpRequestBoard={inpRequestBoard}/> */}
               <button className="black_btn_lg" onClick={createBoard}>
                  글쓰기
               </button>
            </div>

            <table className="board_list">
               <thead>
                  <tr>
                     <th width="60">번호</th>
                     <th>제목</th>
                     <th width="100">작성자</th>
                     <th width="120">날짜</th>
                  </tr>
               </thead>
               <tbody>
                  {posts
                     ? posts.map((post) => (
                          <tr key={post.no}>
                             <td>{post.no}</td>
                             <td
                                className="title_cell"
                                onClick={() => {
                                   gotoBoardDetail(post);
                                }}
                             >
                                {post.title}
                             </td>
                             <td>
                                {post.writer}
                                <img
                                   width="15px"
                                   style={{
                                      verticalAlign: "middle",
                                      marginLeft: "2px",
                                   }}
                                   src={`http://localhost:9999/get.file/${post.img}`}
                                />
                             </td>
                             <td>{post.date}</td>
                          </tr>
                       ))
                     : null}
               </tbody>
            </table>

            <ul>
               <li>
                  <button
                     href="#"
                     onClick={() => {
                        if (1 < count) {
                           let newCount = count - 1;
                           setCount(newCount);
                           const targetPage = newCount * view;
                           setSelectPage(targetPage - 4);
                           requestBoard(targetPage - 4);
                        }
                     }}
                  >
                     &lt;
                  </button>
               </li>

               {pageList()}

               <li>
                  <button
                     onClick={() => {
                        if (count < Math.ceil(allPage / view)) {
                           let newCount = count + 1;
                           setCount(newCount);
                           let targetPage = (newCount - 1) * view + 1;
                           setSelectPage(targetPage);
                           requestBoard(targetPage);
                        }
                     }}
                  >
                     &gt;
                  </button>
               </li>
            </ul>

            {boardView && (
               <div className="modal_overlay">
                  <div className="modal_content">
                     <button
                        className="close_btn"
                        onClick={() => setBoardView(false)}
                     >
                        X
                     </button>

                     <BoardWrite setBoardView={setBoardView} />
                  </div>
               </div>
            )}
         </section>
      </div>
   );
};

export default SecondPage;
