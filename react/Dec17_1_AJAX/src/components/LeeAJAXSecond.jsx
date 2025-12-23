import axios from "axios";
import { useRef, useState } from "react";

const LeeAJAXSecond = () => {
   const inputRef = useRef(null);
   const [documents, setDocuments] = useState(null);
   const onClickFunc = () => {
      axios
         .get(
            `https://dapi.kakao.com/v3/search/book?query=${inputRef.current.value}`,
            {
               headers: {
                  Authorization: "KakaoAK 4728978749201b35c97c6c303ce804b4",
               },
            }
         )
         .then((res) => {
            const resDocuments = res.data.documents;
            setDocuments(resDocuments);
         })
         .then(() => {
            if (inputRef.current) {
               inputRef.current.value = "";
            }
         })
         .catch((err) => {
            alert(err);
         });
   };

   const bookTrs = () =>
      documents.map((d) => {
         return (
            <tr key={d.isbn}>
               <td>
                  <img src={d.thumbnail} alt={d.title} />
               </td>
               <td>{d.authors.join(",")}</td>
               <td>{d.title}</td>
               <td>{d.price}원</td>
            </tr>
         );
      });

   return (
      <div>
         <input ref={inputRef} type="text" />
         <button onClick={onClickFunc}>검색</button>
         <table border={1}>
            <thead>
               <tr>
                  <th>이미지</th>
                  <th>저자</th>
                  <th>제목</th>
                  <th>가격</th>
               </tr>
            </thead>
            <tbody>{documents ? bookTrs() : null}</tbody>
         </table>
      </div>
   );
};

export default LeeAJAXSecond;
