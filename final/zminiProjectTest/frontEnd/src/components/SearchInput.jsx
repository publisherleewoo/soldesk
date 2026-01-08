import { useRef } from "react";

const SearchInput = ({ inpRequestBoard }) => {

   const iptVal = useRef()

   const onClickFunc = () => {
      inpRequestBoard(iptVal.current.value);
   };

   return (
      <div className="search_area">
         <select>
            <option>제목</option>
            <option>작성자</option>
         </select>
         <input type="text" ref={iptVal}placeholder="검색어 입력" />
         <button className="black_btn_sm" onClick={onClickFunc}>
            검색
         </button>
      </div>
   );
};

export default SearchInput;
