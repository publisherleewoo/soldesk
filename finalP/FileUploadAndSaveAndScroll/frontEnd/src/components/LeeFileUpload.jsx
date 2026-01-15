import { useEffect, useRef, useState } from "react";
import { isEmpty, isNotNum, isNotType } from "../lib/leeVailCheckerReact";
import axios from "axios";

const LeeFileUpload = () => {
   const [allPageCount, setAllPageCount] = useState(0);
   const [page, setPage] = useState(1);
   const [product, setProduct] = useState({ name: "", price: "", photo: "" });
   const [products, setProducts] = useState([]);
   const productInput = useRef({});

   const scrollEvent = () => {
      const htmlHeight = document.documentElement.scrollHeight; //총길이
      const brwserHeight = window.innerHeight; //브라우저 길이
      const scrollOffsetTop = window.scrollY; // 스크롤값
      const scrollOffsetBottom = scrollOffsetTop + brwserHeight; //스크롤값+브라우저길이
      if (scrollOffsetBottom >= htmlHeight - 10) {
         setPage(page + 1);
      }
   };

   useEffect(() => {
      window.removeEventListener("scroll", scrollEvent);
      if (page <= allPageCount) {
         axios
            .get(`http://localhost:9999/product.get?page=${page}`)
            .then((res) => {
               setProducts(products.concat(res.data.products));
               setAllPageCount(res.data.pageCount);
               window.addEventListener("scroll", scrollEvent);
            });
      }
   }, [page]);

   useEffect(() => {
      getProduct();
      window.addEventListener("scroll", scrollEvent);
      return () => {
         window.removeEventListener("scroll", scrollEvent);
      };
   }, []);

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
         const productFD = new FormData();
         productFD.append("photo", product.photo);
         productFD.append("name", product.name);
         productFD.append("price", product.price);

         axios
            .post("http://localhost:9999/product.reg ", productFD, {
               headers: { "Content-Type": "multipart/form-data" },
               withCredentials: true,
            })
            .then((res) => {
               alert(JSON.stringify(res.data.result));
               getProduct();
            });
         setProduct({ name: "", price: "", photo: "" });
         productInput.current.photo.value = "";
      }
   };

   var delProduct = (name) => {
      axios
         .get(`http://localhost:9999/product.del?name=${name}`)
         .then((res) => {
            alert(res.data.result);
            getProduct();
         });
   };

   var getProduct = () => {
      axios.get(`http://localhost:9999/product.get?page=1`).then((res) => {
         setProducts(res.data.products);
         setAllPageCount(res.data.pageCount);
      });
   };

   const productsTrs = () => {
      return products.map((p) => {
         const imgUrl = `http://localhost:9999/product.get/${p.photo}`;
         return (
            <tr
               key={p.name}
               onClick={() => {
                  delProduct(p.name);
               }}
            >
               <td>{p.name}</td>
               <td>{p.price}</td>
               <td>
                  <img width={100} src={imgUrl} />
               </td>
            </tr>
         );
      });
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
         <table border={1}>
            <thead>
               <tr>
                  <th>이름</th>
                  <th>가격</th>
                  <th>가격</th>
               </tr>
            </thead>
            <tbody>{products ? productsTrs() : null}</tbody>
         </table>
      </div>
   );
};

export default LeeFileUpload;
