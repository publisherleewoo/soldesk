import { Link, Outlet } from "react-router-dom";
 
import "./siteLayout.css";

const SiteLayout = () => {
   return (
      <>
         <div id="siteLayout">
            <ul>
               <li>
                  <Link to="/">Home</Link>
               </li>
               <li>
                  <Link to="product.go">상품</Link>
               </li>
               <li>
                  <Link to="product2.go">학생</Link>
               </li>
            </ul>
            <Outlet />
         </div>
      </>
   );
};

export default SiteLayout;
