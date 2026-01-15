import axios from "axios";
import { useState } from "react";

const LeeAJAXGET = () => {
   const [xy, setXy] = useState({ x: 0, y: 0 });
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

   const calculate = () => {
      axios
         .get(`http://195.168.9.112:9876/calculator.do?x=${xy.x}&y=${xy.y}`)
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

export default LeeAJAXGET;
