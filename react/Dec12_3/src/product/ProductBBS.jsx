import { useState } from "react";
import "./product.css";
const ProductBBS = () => {
   const [data, setData] = useState([
      { name: "로지텍 G PRO X Superlight", price: 179000 },
      { name: "레이저 Viper V2 Pro", price: 165000 },
      { name: "로지텍 MX Master 3S", price: 119000 },
      { name: "앱코 HACKER A660", price: 29900 },
      { name: "COX CM600", price: 35000 },
   ]);

   const [product, setProduct] = useState({ name: "", price: "" });

   const removeClick = (d) => {
      const newData = data.filter((dd) => {
         return d.name !== dd.name;
      });
      setData(newData);
   };

   const tdData = data.map((d, i) => (
      <tr
         className="dataTr"
         key={i}
         onClick={() => {
            removeClick(d);
         }}
      >
         <td>{d.name}</td>
         <td>{d.price}</td>
      </tr>
   ));

   const changeProduct = (e) => {
      const { name, value } = e.target;
      setProduct({ ...product, [name]: value });
   };
   const regProduct = () => {
      setData(data.concat(product));
      setProduct({ name: "", price: "" });
   };

   return (
      <div id="productBBS">
         품명 :{" "}
         <input
            className="txtType"
            name="name"
            value={product.name}
            onChange={changeProduct}
         />
         <br />
         가격 :{" "}
         <input
            className="txtType"
            name="price"
            value={product.price}
            onChange={changeProduct}
         />
         <br />
         <button onClick={regProduct}>등록</button>
         <hr />
         <table id="productBBSTbl">
            <thead>
               <tr>
                  <th>품명</th>
                  <th>가격</th>
               </tr>
            </thead>
            <tbody>{tdData}</tbody>
         </table>
      </div>
   );
};

export default ProductBBS;
