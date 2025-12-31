import { useDispatch } from "react-redux";
import a from "./img/article.png";
import f from "./img/folder.png";
import i from "./img/image.png";
import w from "./img/windows.png";
import LoginSystem from "./loginSystem/loginSystem";
import { summon } from "../../../slice/loginSystemSummonSlice";

const Menu = () => {
   const d = useDispatch();
   const summonLoginSystem = () => {
      d(summon());
   };
   return (
      <>
         <table id="siteMenuArea">
            <tr>
               <td>
                  <img src={w} onClick={summonLoginSystem} />
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <img src={a} />
                  <img src={f} />
                  <img src={i} />
               </td>
            </tr>
         </table>
         <LoginSystem />
      </>
   );
};

export default Menu;
