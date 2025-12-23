import { Link, useNavigate, useSearchParams } from "react-router-dom";

const LeeP5 = () => {
   const [menu, setMenu] = useSearchParams();
    const n = useNavigate()  //js소스로 이동
   return (
      <div>
         <h1>P5</h1>
         메뉴명 :{menu.get("name")} <br />
         가격 : {menu.get("price")}
         <br />
         <hr />
         <Link to="/p6.go?title=삼국지&price=10000">P6으로</Link>
         <br />
         <Link to="/p6.go?title=파이썬&price=20000">P6으로</Link>
         <button onClick={()=>{
            n("/p6.go?title=리액트&price=30000")
         }}>P6으로</button>
      </div>
   );
};

export default LeeP5;
