import "./WrapLayout.css";
import { Link, Outlet, useNavigate } from "react-router-dom";
import Navigation from "./Navigation";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
// import { tokenCheck } from "../../lib/tokenCheck";
import { setLoginMember } from "../store/memberSlice";


const WrapLayout = () => {
   let d = useDispatch();
   let s = useSelector(store=>store.ms.loginMember)
   let navi = useNavigate()
   useEffect(() => {
    

      // document.addEventListener("click", function () {
      //    tokenCheck(d);
      // });
      // return () => {
      //    document.removeEventListener("click", function () {
      //       tokenCheck(d);
      //    });
      // };
   });

   const loginCheck = () => {
      if (s) {
         return (
            <>
               <Link to="/userInfo">회원정보</Link>
               <button onClick={()=>{
                  sessionStorage.removeItem('loginMember')
                  d(setLoginMember(""))
                  navi('/login')
               }}>로그아웃</button>
               <div><span>{s.id}</span>로그인하다</div>
 
            </>
         );
      } else {
         return (
            <>
               <Link to="/login">로그인</Link>
               <Link to="/signUp">회원가입</Link>
            </>
         );
      } 
   };

   return (
      <div id="WrapLayout">
         <header>
           <br />
            <a className="logo">로고</a>
            <div id="util_nav">{loginCheck()}</div>
            <Navigation />
         </header>
         <aside></aside>
         <section>
            <Outlet />
         </section>
      </div>
   );
};

export default WrapLayout;
