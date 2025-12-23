import { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io.connect("http://195.168.9.86:9999");

function LeeWSClnt() {
   const [msg, setMsg] = useState("");

   useEffect(() => {
      socket.on("test22", (msg22) => {
         alert(msg22);
      });

      return ()=>{
         socket.off("test2");
      }

   }, []);

   const clickFunc = () => {
      socket.emit("test", msg);
      setMsg("");
   };

   return (
      <div>
         <input
            value={msg}
            onChange={(e) => {
               setMsg(e.target.value);
            }}
         ></input>
         <button onClick={clickFunc}>전송</button>
      </div>
   );
}

export default LeeWSClnt;
