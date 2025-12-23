import axios from "axios";
import { useState } from "react";

const LeeAJAXPOST2 = () => {
   const [xy, setXy] = useState({ x: "", y: "" });
   const [result, setResult] = useState({
      hab: null,
      cha: null,
      gob: null,
      moks: null,
   });

   const changeXY = (e) => {
      setXy((prev) => {
         return { ...prev, [e.target.name]: e.target.value };
      });
   };

   const fd = new FormData();
   fd.append("x", xy.x); //fd.append('요청파라메터명',값);
   fd.append("y", xy.y);

   const calculate = () => {
      axios
         .post(`http://195.168.9.112:9876/calculator.do`, fd, {
            withCredentials: true,    //파일,이미지 같은거 보내려고 post쪽에 넣을때 이것 포함되어야함. 
         })
         .then((res) => {
            setResult(res.data);
         })
         .catch((err) => alert(err));
   };

   return (
      <div>
         x:
         <input value={xy.x} name="x" onChange={changeXY} />
         <br />
         y:
         <input value={xy.y} name="y" onChange={changeXY} />
         <br />
         <br />
         <button onClick={calculate}>계산</button>
         <hr />
         합:{result.hab}
         <br />
         차:{result.cha}
         <br />
         곱:{result.gob}
         <br />
         몫:{result.moks}
         <br />
      </div>
   );
};

export default LeeAJAXPOST2;
