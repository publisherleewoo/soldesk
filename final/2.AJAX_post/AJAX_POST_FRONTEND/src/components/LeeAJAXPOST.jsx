import axios from "axios";
import { useState } from "react";

const LeeAJAXPOST = () => {
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
         .post(`http://195.168.9.112:9876/calculator.do`, fd)
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

export default LeeAJAXPOST;
