import { useSelector } from "react-redux";

//subscriber : redux state를 사용할 존재
const LeeH1 = () => {
   // 설정8  useSelectrot 설정(전역인 main.jsx에 등록된 스토어.리듀서속성명   (reducer안에있는 키값))
   const h1CSS = useSelector((store)=>store.lss);
   const text = useSelector((store)=>store.tss);
   return (
      <div>
         <h1 style={{fontSize:h1CSS.fontSize}}>{text.val? text.val:"ㅋㅋㅋㅋ"}</h1>
      </div>
   );
};

export default LeeH1;
