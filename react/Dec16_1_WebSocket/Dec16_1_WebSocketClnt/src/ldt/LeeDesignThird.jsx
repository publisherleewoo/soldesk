import { useEffect } from "react";
import ldtmc from "./ldt.module.css";

const LeeDesignThird = () => {
   useEffect(() => {
      const h = 180;
      const w = 80;

      alert(`키는 ${h}cm고, 몸무게는 ${w}kg다`);

      return () => {};
   }, []);
   return <div className={`${ldtmc.a} ${ldtmc.b} ${ldtmc.c}`}>LeeDesignThird</div>;
};

export default LeeDesignThird;
