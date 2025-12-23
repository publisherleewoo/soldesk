import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";

const LeeP2 = () => {
   const [product, setProduct] = useState({
      name: "",
      price: "",
   });

   const changeProduct = (e) => {
      setProduct({ ...product, [e.target.name]: e.target.value });
   };

   const regProduct = () => {
      axios
         .get(
            `http://localhost:9999/product.reg?name=${product.name}&price=${product.price}`
         )
         .then((res) => {
            sessionStorage.setItem("productInfo", res.data.token);
         });
   };

   return (
      <div>
         <h1>P2페이지</h1>
         품명 :{" "}
         <input name="name" value={product.name} onChange={changeProduct} />
         <br />
         가격 :{" "}
         <input name="price" value={product.price} onChange={changeProduct} />
         <br />
         <button onClick={regProduct}>등록</button>
         <hr></hr>
         <Link to="/p3.go">p3로</Link>
      </div>
   );
};

export default LeeP2;
