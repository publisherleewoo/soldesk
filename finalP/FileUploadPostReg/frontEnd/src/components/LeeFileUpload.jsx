import { useRef, useState } from "react";
import { isEmpty, isNotNum, isNotType } from "../lib/leeVailCheckerReact";
import axios from "axios";

const LeeFileUpload = () => {
   const [product, setProduct] = useState({ name: "", price: "", photo: "" });
   const productInput = useRef({});
   const changeProduct = (e) => {
      if (e.target.name === "photo") {
         setProduct({ ...product, photo: e.target.files[0] });
      } else {
         setProduct({ ...product, [e.target.name]: e.target.value });
      }
   };

   const isValid = () => {
      if (isEmpty(product.name)) {
         alert("제품명?");
         productInput.current.name.value = "";
         productInput.current.name.focus();
         return false;
      }

      if (isEmpty(product.price) || isNotNum(product.price)) {
         alert("가격?");
         productInput.current.price.value = "";
         productInput.current.price.focus();
         return false;
      }

      if (
         isEmpty(product.photo) ||
         (isNotType(product.photo, "png") &&
            isNotType(product.photo, "gif") &&
            isNotType(product.photo, "jpg"))
      ) {
         alert("사진?");
         productInput.current.photo.value = "";

         return false;
      }

      return true;
   };

   const regProduc = () => {
      if (isValid()) {
         const FormDataSet = new FormData();
         FormDataSet.append("name", product.name);
         FormDataSet.append("price", product.price);
         FormDataSet.append("photo", product.photo);
         axios
            .post("http://localhost:9999/pic.post", FormDataSet, {
               headers: {
                  "Content-Type": "multipart/form-data",
               },
            })
            .then((res) => {
               console.log(res.data);
            })
            .catch((err) => {
               alert(err);
            });

         setProduct({ name: "", price: "", photo: "" });
         productInput.current.photo.value = "";
      }
   };

   return (
      <div>
         <input
            name="name"
            value={product.name}
            ref={(thisInput) => {
               productInput.current.name = thisInput;
            }}
            onChange={changeProduct}
         />
         <br />
         <input
            name="price"
            value={product.price}
            ref={(thisInput) => {
               productInput.current.price = thisInput;
            }}
            onChange={changeProduct}
         />
         <br />
         <input
            type="file"
            name="photo"
            ref={(thisInput) => {
               productInput.current.photo = thisInput;
            }}
            onChange={changeProduct}
         />
         <br />
         <button onClick={regProduc}>버튼</button>
         <hr />
         <table>
            <thead>
               <tr>
                  <th>이름</th>
                  <th>가격</th>
                  <th>사진</th>
               </tr>
            </thead>
         </table>
      </div>
   );
};

export default LeeFileUpload;
