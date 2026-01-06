 
import "./App.css";
import Main from "./router/Main";
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { useTokenCheck } from "../lib/useTokenCheck";

function App() {
 
   const location = useLocation();
   const check = useTokenCheck();
   
   useEffect(()=>{
       check()
   },[location.pathname])

   return (
      <div id="Main">
         <Main />
      </div>
   );
}

export default App;
