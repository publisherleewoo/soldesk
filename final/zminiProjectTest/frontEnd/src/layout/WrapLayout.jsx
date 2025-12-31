import "./WrapLayout.css";
import { Link, Outlet } from "react-router-dom";
import Navigation from "./Navigation";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { tokenCheck } from "../../lib/tokenCheck";

const WrapLayout = () => {
   let d = useDispatch();
   useEffect(() => {
      document.addEventListener("click", function () {
         tokenCheck(d);
      });
      return () => {
         document.removeEventListener("click", function () {
            tokenCheck(d);
         });
      };
   });

   const token = useSelector((store) => {
      return store.ms.loginMember;
   });
   const loginCheck = () => {
      if (typeof token === "object" && Object.keys(token).length === 0) {
         return (
            <>
               <Link to="/login">로그인</Link>
               <Link to="/signUp">회원가입</Link>
            </>
         );
      } else {
         return <>
               <Link to="/userInfo">회원정보</Link>
               <button>로그아웃</button>
         
         </>;
      }
   };

   return (
      <div id="WrapLayout">
         <header>
            WrapLayout <br />
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
