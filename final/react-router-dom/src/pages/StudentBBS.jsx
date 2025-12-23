import { useState } from "react";
const StudentBBS = () => {
   const [data, setData] = useState([
      { name: "홍길동", age: 15 },
      { name: "김길동", age: 14 },
      { name: "이길동", age: 26 },
      { name: "강길동", age: 25 },
      { name: "우길동", age: 34 },
   ]);

   const [product, setProduct] = useState({ name: "", age: "" });

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
         <td>{d.age}</td>
      </tr>
   ));

   const changeProduct = (e) => {
      const { name, value } = e.target;
      setProduct({ ...product, [name]: value });
   };
   const regProduct = () => {
      setData(data.concat(product));
      setProduct({ name: "", age: "" });
   };

   return (
      <div id="StudentBBS">
         이름 :{" "}
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
            name="age"
            value={product.age}
            onChange={changeProduct}
         />
         <br />
         <button onClick={regProduct}>등록</button>
         <hr />
         <table id="StudentBBSTbl">
            <thead>
               <tr>
                  <th>이름</th>
                  <th>나이</th>
               </tr>
            </thead>
            <tbody>{tdData}</tbody>
         </table>
      </div>
   );
};

export default StudentBBS;
