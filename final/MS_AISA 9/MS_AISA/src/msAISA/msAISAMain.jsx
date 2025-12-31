import Content from "./layout/content/content";
import Menu from "./layout/menu/menu";
import Title from "./layout/title/title";
import "./layout/layout.css";
import "./layout/menu/loginSystem/login.css";
import "./layout/content/member/member.css";
import { useEffect } from "react";
import axios from "axios";
import { setLoginMember } from "../slice/memberSlice";
import { useDispatch } from "react-redux";

let d = null;
// eslint-disable-next-line react-refresh/only-export-components
export const loginCheck = () => {
   axios
      .get(
         `http://localhost:9999/member.info.get?member=${sessionStorage.getItem(
            "loginMember"
         )}`
      )
      .then((res) => {
         d(setLoginMember(res.data.member));
         if (res.data.member === undefined) {
            // 로그인 풀렸으면
         } else {
            axios
               .get(
                  `http://localhost:9999/sign.in.exp.refresh?member=${sessionStorage.getItem(
                     "loginMember"
                  )}`
               )
               .then((res2) => {
                  sessionStorage.setItem("loginMember", res2.data.member);
               });
         }
      });
};

const MSAISAMain = () => {
   // eslint-disable-next-line react-hooks/globals
   d = useDispatch();

   useEffect(() => {
      document.addEventListener("click", loginCheck);

      return () => {
         document.removeEventListener("click", loginCheck);
      };
   }, []);

   return (
      <>
         <Title />
         <Content />
         <Menu />
      </>
   );
};

export default MSAISAMain;
