import { NavLink } from "react-router-dom";
import "./Navigation.css";

const Navigation = () => {
   return (
      <nav id="globalNavi">
         <ul>
            <li>
               <NavLink
                  to="/"
                  className={({ isActive }) => (isActive ? "active" : "")}
               >
                  홈
               </NavLink>
            </li>
            <li>
               <NavLink
                  to="/b"
                  className={({ isActive }) => (isActive ? "active" : "")}
               >
                  b
               </NavLink>
            </li>
            <li>
               <NavLink
                  to="/c"
                  className={({ isActive }) => (isActive ? "active" : "")}
               >
                  c
               </NavLink>
            </li>
            <li>
               <NavLink
                  to="/d"
                  className={({ isActive }) => (isActive ? "active" : "")}
               >
                  d
               </NavLink>
            </li>
         </ul>
      </nav>
   );
};

export default Navigation;
