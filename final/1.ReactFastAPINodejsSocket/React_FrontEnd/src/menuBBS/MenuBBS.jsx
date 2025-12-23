import { useCallback, useRef, useState } from "react";
import "./Menu.css";
import { isEmpaty } from "../lib/leeVailCheckerReact";

const MenuBBS = () => {
   const [menu, setMenu] = useState({ name: "", price: "", desc: "" });

   const nameInput = useRef();
   const priceInput = useRef();
   const descInput = useRef();

   const onChange = useCallback((e) => {
      setMenu((preveMenu) => ({
         ...preveMenu,
         [e.target.name]: e.target.value,
      }));
   }, []);

   const regMenu = () => {
      if (isValid()) {
         alert("Ajax출발");
      }
   };

   const isValid = () => {
      if (isEmpaty(menu.name)) {
         alert("메뉴명?");
         nameInput.current.value = "";
         nameInput.current.focus();
         return false;
      }
      if (isEmpaty(menu.price) || menu.price < 0) {
         alert("메뉴가격?");
         priceInput.current.value = "";
         priceInput.current.focus();
         return false;
      }
      if (isEmpaty(menu.desc)) {
         alert("설명?");
         descInput.current.value = "";
         descInput.current.focus();
         return false;
      }

      return true;
   };

   return (
      <div id="MenuBBS">
         메뉴명 :{" "}
         <input
            ref={nameInput}
            name="name"
            onChange={onChange}
            maxLength={30}
            required
         />
         <br />
         가격 : <input ref={priceInput} name="price" onChange={onChange} />
         <br />
         설명 : <input ref={descInput} name="desc" onChange={onChange} />
         <button onClick={regMenu}>등록</button>
         <hr />
         <table border={1}>
            <tbody>
               <tr>
                  <td>메뉴명메뉴명</td>
                  <td>가격가격가격가격</td>
                  <td>설명설명설명설명</td>
               </tr>
            </tbody>
         </table>
      </div>
   );
};

export default MenuBBS;
