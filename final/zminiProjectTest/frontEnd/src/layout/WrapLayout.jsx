import "./WrapLayout.css";
import { Link, Outlet } from "react-router-dom";
import Navigation from "./Navigation";

const WrapLayout = () => {
   return (
      <div id="WrapLayout">
         <header>
            WrapLayout <br />
            <a className="logo">로고</a>
            <div id="util_nav">
               <Link to="/login">로그인</Link>
               <Link to="/signUp">회원가입</Link>
            </div>
            <Navigation />
         </header>
         <aside>

         </aside>
         <section>
            <Outlet />
         </section>
      </div>
   );
};

export default WrapLayout;
