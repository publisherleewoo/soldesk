import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import "./Menu.css";
import { isEmpaty, isNotNum } from "../lib/leeVailCheckerReact";
import axios from "axios";
import LiComponent from "./LiComponent";
import io from "socket.io-client";

const socket = io("http://195.168.9.112:9999");

const MenuBBS2 = () => {
   const [menu, setMenu] = useState({ name: "", price: "", desc: "" });
   const [data, setData] = useState([]);
   const [pageCount, setPageCount] = useState(1);
   const [nowPage, setNowPage] = useState(1);

   const menuInput = useRef({
      name: null,
      price: null,
      desc: null,
   });
   // 버튼 누른 숫자의 값을 스테이트에 저장해서 getMenu(안에 넣기)

   useEffect(() => {
      getMenu(nowPage);
      socket.on("updatedSrv", function () {
         getMenu(nowPage);
      });

      return () => {
         socket.off("updatedSrv");
      };
   }, [getMenu, nowPage]);

   var getMenu = useCallback((pageNo) => {
      setNowPage(pageNo);
      axios
         .get(`http://195.168.9.112:8888/menu.get?pageNo=${pageNo}`)
         .then((res) => {
            const resData = res.data;
            setData(resData.Menus);
            setPageCount(resData.allPageCount);
         })
         .catch((err) => alert(err));
   }, []);

   const onChange = useCallback((e) => {
      setMenu((preveMenu) => ({
         ...preveMenu,
         [e.target.name]: e.target.value,
      }));
   }, []);

   const regMenu = () => {
      const { name, price, desc } = menuInput.current;

      if (isValid()) {
         axios
            .get(
               `http://195.168.9.112:8888/menu.reg?name=${name.value}&price=${price.value}&desc=${desc.value}`
            )
            .then((res) => {
               alert(res.data.msg);
               // debugger
               if (res.data.msg === "등록성공") {
                  socket.emit("updated", "reg");
                  getMenu(nowPage);
               }

               menuInput.current.name.value = "";
               menuInput.current.price.value = "";
               menuInput.current.desc.value = "";
            })
            .catch((err) => alert(err));
      }
   };

   const isValid = () => {
      if (isEmpaty(menu.name)) {
         alert("메뉴명?");
         menuInput.current.name.value = "";
         menuInput.current.name.focus();
         return false;
      }
      if (isEmpaty(menu.price) || isNotNum(menu.price) || menu.price < 0) {
         alert("메뉴가격?");
         menuInput.current.price.value = "";
         menuInput.current.price.focus();
         return false;
      }
      if (isEmpaty(menu.desc)) {
         alert("설명?");
         menuInput.current.desc.value = "";
         menuInput.current.desc.focus();
         return false;
      }
      return true;
   };

   const listFunc = useMemo(() => {
      let items = [];
      for (let i = 1; i <= pageCount; i++) {
         items.push(
            <LiComponent key={i} i={i} getMenu={getMenu}>
               {i}
            </LiComponent>
         );
      }
      return <ul>{items}</ul>;
   }, [pageCount, getMenu]);

   return (
      <div id="MenuBBS">
         메뉴명 :{" "}
         <input
            ref={(thisInput) => {
               return (menuInput.current.name = thisInput);
            }}
            name="name"
            onChange={onChange}
            maxLength={30}
            required
         />
         <br />
         가격 :{" "}
         <input
            ref={(thisInput) => {
               return (menuInput.current.price = thisInput);
            }}
            name="price"
            onChange={onChange}
         />
         <br />
         설명 :{" "}
         <input
            ref={(thisInput) => {
               return (menuInput.current.desc = thisInput);
            }}
            name="desc"
            onChange={onChange}
         />
         <button onClick={regMenu}>등록</button>
         <hr />
         <table border={1}>
            <thead>
               <tr>
                  <th>메뉴명</th>
                  <th>가격</th>
                  <th>설명</th>
               </tr>
            </thead>
            <tbody>
               {data &&
                  data.map((d, i) => {
                     return (
                        <tr key={i}>
                           <td>{d.n}</td>
                           <td>{d.p}</td>
                           <td>{d.d}</td>
                        </tr>
                     );
                  })}
            </tbody>
         </table>
         {listFunc}
      </div>
   );
};

export default MenuBBS2;
