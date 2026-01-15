import React from "react";
import { Link, useSearchParams } from "react-router-dom";

const LeeP6 = () => {
   const [book, setBook] = useSearchParams();
   return (
      <div>
         <h1>P6</h1>
         제목:{book.get("title")}
         <br />
         가격:{book.get("price")}
         <br/>
         <Link to="/p7.go">p7가기</Link>
      </div>
   );
};

export default LeeP6;
