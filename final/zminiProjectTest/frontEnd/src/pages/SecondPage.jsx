import { useEffect, useState } from "react";
import "./SecondPage.css";
import axios from "axios";
import BoardWrite from "../components/BoardWrite";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setPostSlice } from "../store/boardSlice";

const SecondPage = () => {
   const [posts, setPosts] = useState("");
   const [allPage, setAllPage] = useState(0);
   const [selectPage, setSelectPage] = useState(1);

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
   }, [d, boardView]);

   const createBoard = () => {
      //로그인이 안되어있으면 메인으로,
      //상세페이지에 갔는데도 로그인이 안되어있으면 메인으로
      setBoardView(true);
   };

   const gotoBoardDetail = (post) => {
      navi(`/b/${post.no}`);
      d(setPostSlice(post));
   };

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
      for (let i = 1; i <= allPage; i++) {
         let newlist = (
            <li>
               <a
                  href="#"
                  className={selectPage == i ? "active" : null}
                  onClick={() => {
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
               <div className="search_area">
                  <select>
                     <option>제목</option>
                     <option>작성자</option>
                  </select>
                  <input type="text" placeholder="검색어 입력" />
                  <button className="black_btn_sm">검색</button>
               </div>
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

            <ul>{pageList()}</ul>

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
