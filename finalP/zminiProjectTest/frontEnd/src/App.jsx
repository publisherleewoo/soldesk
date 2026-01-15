import "./App.css";
import Main from "./router/Main";
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { useTokenCheck } from "../lib/useTokenCheck";

function App() {
   const location = useLocation();
   const check = useTokenCheck();

   useEffect(() => {
      const memberId = sessionStorage.getItem("loginMember");
    
      if (memberId) {
         check(memberId);
      }
   }, [location.pathname]);

   return (
      <div id="Main">
         <Main />
      </div>
   );
}

export default App;
