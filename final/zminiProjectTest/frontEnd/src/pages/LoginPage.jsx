import { useRef } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./LoginPage.css";
import axios from "axios";
import { setLoginMember } from "../store/memberSlice";
import { useDispatch } from "react-redux";
const LoginPage = () => {
   const idInput = useRef();
   const pwdInput = useRef();
   const d=  useDispatch()
   const navi = useNavigate()

   const handleLoign = () => {
      const inCnt = idInput.current;
      const pwdCnt = pwdInput.current;
      const fd = new FormData();
      fd.append("id", inCnt.value);
      fd.append("pwd", pwdCnt.value);



      axios
         .post("http://localhost:9999/login", fd, { withCredentials: true })
         .then((res) => {
            if (res.data.msg === "로그인 성공") {
               alert(res.data.msg);
               sessionStorage.setItem("loginMember", res.data.memberToken);
               d(setLoginMember(res.data.member))
               // token값이 아니라 최소한의 로그인 정보를 담아야한다. 위의 res.data.member는 token값임
               navi("/")
            }else{
               alert(res.data.msg)
            }
         })
         .catch((err) => alert(err));
   };

   return (
      <div id="LoginWrap">
         <div>
            <h3>Login</h3>

            <div className="row">
               <label>ID</label>
               <input
                  type="text"
                  className="id_input"
                  ref={idInput}
                  placeholder="아이디 입력" onKeyUp={(e)=>e.code === 'Enter' ? handleLoign():null}
               />
            </div>

            <div className="row">
               <label>PW</label>
               <input
                  type="password"
                  ref={pwdInput}
                  placeholder="비밀번호 입력"   onKeyUp={(e)=>e.code === 'Enter' ? handleLoign():null}
               />
            </div>

            <div className="btn_area">
               <button
                  type="button"
                  className="submit_btn"
                  onClick={handleLoign}
               
               >
                  로그인
               </button>

               {/* 하단 보조 링크 영역 */}
               <div className="sub_links">
                  <Link to="/signUp" className="link_text">
                     회원가입
                  </Link>
                  <span className="split_bar">|</span>
                  <Link to={-1} className="link_text">
                     뒤로가기
                  </Link>
               </div>
            </div>
         </div>
      </div>
   );
};

export default LoginPage;

