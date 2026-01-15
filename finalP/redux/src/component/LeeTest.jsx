import { useState } from "react";

const LeeTest = () => {
   const [h1CSS, seth1CSS] = useState({ fontSize: 30 });
   u
   const sizeUp = () => {
      seth1CSS({ fontSize: h1CSS.fontSize + 5 });
   };

   const sizeDown = () => {
      seth1CSS({ fontSize: h1CSS.fontSize - 5 });
   };

   return (
      <div>
         <button onClick={sizeUp}>크게</button>
         <button onClick={sizeDown}>작게</button>
         <h1 style={h1CSS}>ㅋㅋㅋ</h1>
         <br />
      </div>
   );
};

export default LeeTest;
