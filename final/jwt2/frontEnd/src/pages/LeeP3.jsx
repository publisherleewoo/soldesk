import axios from "axios";
import { Link } from "react-router-dom";

const LeeP3 = () => {
   const showProduct = () => {
      axios
         .get(
            `http://localhost:9999/product.get?token=${sessionStorage.getItem(
               "productInfo"
            )}`
         )
         .then((res) => {
 
            alert(res.data.name + ":" + res.data.price);
         });
   };

   return (
      <div>
         <h1>p3</h1>
         <button onClick={showProduct}>등록한거 확인</button>
         <hr/>
         <Link to="/p4.go/홍길동/30">P4로</Link><br/>
         <Link to="/p4.go/김길동/20">P4로</Link><br/>
         <a href="/p4.go/이길동/10">p4로</a><br/>
 
      </div>
   );
};

export default LeeP3;
